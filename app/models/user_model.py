from env.database import database


class user_model:
    def get_user(self):
        conn = database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        data = cursor.fetchall()
        return data

    def insert(self,user,email,password):
        conn = database.connect()
        cursor = conn.cursor()
        result = cursor.execute(
            """INSERT INTO user (
                    username,
                    email,
                    password
                ) 
                VALUES (%s,%s,%s)""",(user,email,password))
        if(result):
            conn.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False

    def update(self,id,user,email,password):
        conn = database.connect()
        cursor = conn.cursor()
        result = cursor.execute("UPDATE user SET username = %s, email = %s, password = %s WHERE id = %s",(user,email,password,int(id)))
        conn.commit()
        conn.close()
        return result

    def delete(self,id):
        conn = database.connect()
        cursor = conn.cursor()
        result = cursor.execute("DELETE FROM user WHERE id = %s",int(id))
        conn.commit()
        conn.close()
        return result