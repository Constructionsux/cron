import mysql.connector 
from dotenv import load_dotenv

load_dotenv()

def get_db():
  return mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user =  os.getenv("DB_USER"),
        password =  os.getenv("DB_PASSWORD"),
        database =  os.getenv("DB_NAME"), 
        port =  os.getenv("DB_PORT"),
)


def check_overdue_invoices():
     conn = get_db()
     cursor = conn.cursor()

     try:
          cursor.execute(
          """
          UPDATE invoices
          SET status='overdue'
          WHERE due_date < NOW() AND status IN ('pending', 'unpaid')
          """
          )
          conn.commit()
          print("Overdue invoices updated")
     finally:
          cursor.close()
          conn.close()
