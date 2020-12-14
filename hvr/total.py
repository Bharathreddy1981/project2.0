def total(db):

    cursor = db.cursor()

    try:
        query = "select * from user"
        cursor.execute(query)
        red = cursor.fetchall()
        login_list11 = []
        for i in red:
            k = {"name": i[0], "email": i[1], "role_type": i[2], "phone": i[3]}
            login_list11.append(k)


    except Exception as e:
        return {'Error': str(e)}

    return {"data": login_list11}