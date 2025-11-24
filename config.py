def db_config():
    hots = input("Enter your host")
    user = input("Enter user name")
    password = input("Enter password")
    database = input("Enter database name")
    dict1 = {
        "host":hots,
        "user":user,
        "password":password,
        "database":database
    }
    return dict1