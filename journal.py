import psycopg2
from datetime import datetime

def save_journal_entry(entry):
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname="robbiechristian", 
        user="robbiechristian", 
        password="9700", 
        host="localhost"
    )
    cursor = conn.cursor()

    # Get the current timestamp
    now = datetime.now()

    # Insert the new entry into the journal_entries table
    cursor.execute("INSERT INTO journal_entries (entry, entry_timestamp) VALUES (%s, %s)", (entry, now))

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()

# Example usage
save_journal_entry("Today's journal entry...")
