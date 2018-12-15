from api.connection import my_conn

def check_token(connection_token) -> bool:
    return True
    my_cur = my_conn.cursor() 
    my_cur.execute(f"""
    SELECT * FROM players WHERE connection_token='{connection_token}' LIMIT 1;
    """)
    row = my_cur.fetchall()
    my_cur.close()
    return len(row) >= 1