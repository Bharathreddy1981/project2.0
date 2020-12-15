
def update(db, values, post_data, validations_data):
    if post_data != validations_data:
        return validations_data
    else:
        name = post_data['name']
        phone = post_data['phone']
        #email = post_data['email']
        role = post_data['role_name']
        cursor = db.cursor()

    query11 = "select * from user where  email ='" + str(values) + "'"
    cursor.execute(query11)
    db.commit()
    red = cursor.fetchall()
    login_list11 = []
    for i in red:
        k = {"name": i[0], "email": i[1], "role_type": i[2], "phone": i[3]}
        login_list11.append(k)
    if len(login_list11) == 0:
        return {"email": "The email does not exists to update the values"}

    try:
        query = "UPDATE user SET  name = ('" + str(name) + "'), role_type = ('" + str(role) + "'), phone_number = ('" + str(phone) + "') where email = '" + str(values) + "'"
        cursor.execute(query)
        db.commit()
    except Exception as e:
        return {'Error': str(e)}

    return {"User": 'updated User successfully'}
