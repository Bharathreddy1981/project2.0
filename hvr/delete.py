
def delete(db, post_data):

    email = post_data['email']

    cursor = db.cursor()

    try:
        query = "delete from user where email = '" + str(email) + "'"
        cursor.execute(query)
        db.commit()
    except Exception as e:
        return {
            'Error': str(e).split()[1].replace('\"', '') + " " + str(e).split()[2] + " " + str(e).split()[-1].replace(
                "'register_table.", "").replace("'", "").replace('\")', '').replace('user.', '')}

    return {"User": 'deleted User successfully'}

