import psycopg2

def get_connection():
    return psycopg2.connect(
        host="**enter_your_hostname**",
        database="crm_system",
        user="postgres",
        password="admin123"
    )
print("Connection Done")
