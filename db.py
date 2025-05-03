import psycopg2

def get_connection():
    """
    Establishes a connection to the PostgreSQL database using the provided credentials.
    It returns a psycopg2 connection object if the connection is successful.
    Ensure that the hostname, database name, username, and password are
    correctly configured for your PostgreSQL server.
    """
    return psycopg2.connect(
        host="enter_your_hostname",
        database="crm_system",
        user="postgres",
        password="enter_your_server_password/master_password"
    )

print("Connection Done") # This line will be executed after the get_connection function is defined.
                        # It does NOT necessarily mean that a database connection has been successfully
                        # established. The connection is only attempted when the get_connection()
                        # function is actually called later in the script.
