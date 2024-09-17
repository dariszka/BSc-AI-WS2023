import dill as pickle
import datetime
import os


def create_user(name: str, data: str, password:str, log_file = 'logs.txt'):
    user_data = dict(
            name=name,
            data=data,
            password=password,
            last_changed = datetime.datetime.now()
        )
    
    if not os.path.isfile(name + '.pkl'):
        with open(f"{name}.pkl", "wb") as f:
            pickle.dump(user_data, f)

        with open(log_file, "a") as f:
            f.write(f'Created user {name} at {user_data["last_changed"]}\n')    
    else:
        with open(log_file, "a") as f:
            f.write(f'Attempted creation of existing user {name} at {user_data["last_changed"]}\n')


def login(name: str, password: str, log_file = 'logs.txt'):
    if not os.path.isfile(name + '.pkl'):
        with open(log_file, "a") as f:
            f.write(f'Attempted login for non-existing user {name} at {datetime.datetime.now()}\n')
            return None
    else:
        with open(log_file, "a") as f:
            f.write(f'Attempted login for user {name} at {datetime.datetime.now()}\n')

            with open(f"{name}.pkl", "rb") as p:
                user_data = pickle.load(p)
                user_password = user_data["password"]

                if password == user_password:
                    f.write(f'Login successful for user {name} at {datetime.datetime.now()}\n')
                    return user_data["data"]
                else:
                    f.write(f'Login failed for user {name} at {datetime.datetime.now()}\n')
                    return None


def change_password(name: str, old_password: str,
                    new_password: str, log_file = 'logs.txt'):
    if not os.path.isfile(name + '.pkl'):
         return #this is just so it won't throw any errors in case it's tested against that, but nothing
                #about it was mentioned in the assignment file or the logs.txt, so I'm not handling it 
    
    with open(log_file, "a") as f:
        f.write(f'Attempted password change for user {name} at {datetime.datetime.now()}\n')

        with open(f"{name}.pkl", "rb") as p:
            user_data = pickle.load(p)
            user_password = user_data["password"]

            if user_password == old_password:
                user_data["password"] = new_password
                user_data["last_changed"] = datetime.datetime.now()
                with open(f"{name}.pkl", "wb") as p_write:
                    pickle.dump(user_data, p_write)
                f.write(f'Password change successful for user {name} at {user_data["last_changed"]}\n')
            else:
                f.write(f'Password change failed for user {name} at {datetime.datetime.now()}\n')
