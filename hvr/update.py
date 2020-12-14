
def update(db, post_data, validations_data):
    if post_data != validations_data:
        return validations_data
    else:
        name = post_data['name']
        phone = post_data['phone']
        email = post_data['email']
        role = post_data['role_name']
        cursor = db.cursor()

    try:
        query = "UPDATE user SET  name = ('" + str(name) + "'), role_type = ('" + str(role) + "'), phone_number = ('" + str(phone) + "') where email = '" + str(email) + "'"
        cursor.execute(query)
        db.commit()
    except Exception as e:
        return {
            'Error': str(e).split()[1].replace('\"', '') + " " + str(e).split()[2] + " " + str(e).split()[-1].replace(
                "'register_table.", "").replace("'", "").replace('\")', '').replace('user.', '')}

    return {"User": 'updated User successfully'}
