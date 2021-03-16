class LogInTemp:

    instance = None

    def __new(cls, *args, **kwargs):
        if not isinstance(cls.instance,cls):
            cls.__instance = super(LogInTemp,cls).__new(cls)
        else:
            print("Object of LogIn is already created")
        return cls.instance

    def log(self):
        log_in = input("Enter login: ")
        password = input("Enter password: ")
        print(f"You logged in like {log_in}")




if __name__ == "main":
    login = LogInTemp()
    login.log()
    login2 = LogInTemp()
    login2.log()

    #23
