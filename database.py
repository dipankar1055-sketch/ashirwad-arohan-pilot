import sqlite3
import pandas as pd
from datetime import datetime
import config
import os

DB_PATH = "data/ashirwad_arohan.db"

def get_connection():
    """Get database connection"""
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db():
    """Initialize database tables"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create members table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            membership_id TEXT UNIQUE,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            address TEXT,
            children_below_5 INTEGER DEFAULT 0,
            children_5_12 INTEGER DEFAULT 0,
            adults INTEGER DEFAULT 1,
            membership_type TEXT,
            amount INTEGER,
            payment_date TEXT,
            donation_amount INTEGER DEFAULT 0,
            payment_status TEXT DEFAULT 'Pending',
            followup_status TEXT DEFAULT 'Not Updated',
            committee_interest TEXT,
            comments TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create donations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS donations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            donor_name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            amount INTEGER NOT NULL,
            message TEXT,
            status TEXT DEFAULT 'Pending',
            trace_id TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,
            amount INTEGER,
            status TEXT DEFAULT 'Pending',
            trace_id TEXT,
            hat_id TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def import_members_from_excel(excel_path):
    """Import members from Excel file"""
    if not os.path.exists(excel_path):
        return False
    
    df = pd.read_excel(excel_path, sheet_name="Aarohan Durga Puja 2026")
    conn = get_connection()
    cursor = conn.cursor()
    
    count = 0
    for idx, row in df.iterrows():
        if pd.isna(row.get('Name')):
            continue
        
        membership_type = row.get('Membership Type', config.DEFAULT_MEMBERSHIP_TYPE)
        if pd.isna(membership_type):
            membership_type = config.DEFAULT_MEMBERSHIP_TYPE
        
        amount = row.get('Amount (INR)', config.DEFAULT_AMOUNT)
        if pd.isna(amount):
            amount = config.DEFAULT_AMOUNT
        
        membership_id = config.MEMBERSHIP_ID_FORMAT.format(id=idx+1)
        
        cursor.execute('''
            INSERT OR IGNORE INTO members (
                membership_id, name, email, phone, address,
                children_below_5, children_5_12, adults,
                membership_type, amount, payment_date,
                donation_amount, payment_status, followup_status,
                committee_interest, comments
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            membership_id,
            str(row.get('Name', '')),
            str(row.get('Email', '')),
            str(row.get('Mobile Number', '')),
            str(row.get('Address', '')),
            int(row.get('Children Below 5', 0)),
            int(row.get('Children 5-12', 0)),
            int(row.get('Adults', 1)),
            str(membership_type),
            int(amount),
            str(row.get('Payment Date', '')),
            int(row.get('Donation Amount', 0)),
            str(row.get('Payment Status', config.DEFAULT_PAYMENT_STATUS)),
            str(row.get('Status', config.DEFAULT_FOLLOWUP_STATUS)),
            str(row.get('Committee Interest', '')),
            str(row.get('Comments', ''))
        ))
        count += 1
    
    conn.commit()
    conn.close()
    return count

def add_member(data):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM members")
    count = cursor.fetchone()[0] + 1
    membership_id = config.MEMBERSHIP_ID_FORMAT.format(id=count)
    
    cursor.execute('''
        INSERT INTO members (
            membership_id, name, email, phone, address,
            children_below_5, children_5_12, adults,
            membership_type, amount, payment_status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        membership_id,
        data['name'],
        data['email'],
        data['phone'],
        data['address'],
        data.get('children_below_5', 0),
        data.get('children_5_12', 0),
        data.get('adults', 1),
        data['membership_type'],
        data['amount'],
        'Pending'
    ))
    
    conn.commit()
    conn.close()
    return membership_id

def get_all_members():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM members ORDER BY id", conn)
    conn.close()
    return df

def get_dashboard_stats():
    conn = get_connection()
    cursor = conn.cursor()
    
    stats = {}
    cursor.execute("SELECT COUNT(*) FROM members")
    stats['total_members'] = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT COUNT(*) FROM members WHERE DATE(created_at) = DATE('now')")
    stats['today_registrations'] = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT SUM(amount) FROM members WHERE payment_status = 'Payment Made'")
    stats['total_membership_fees'] = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT SUM(donation_amount) FROM members")
    stats['total_donations'] = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT COUNT(*) FROM members WHERE payment_status = 'Pending'")
    stats['pending_payments'] = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT COUNT(*) FROM members WHERE membership_type LIKE '%Existing%' AND payment_status = 'Pending'")
    stats['renewals_due'] = cursor.fetchone()[0] or 0
    
    conn.close()
    return stats
