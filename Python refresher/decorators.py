user = {"username": "jose", "access_level": "guest"}

## one way to do it
def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f"No way {user['username']}!"
    return secure_function

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())

## a better way to do it
@make_secure
def get_admin_password():
    return "1234"
user = {"username": "Hans", "access_level": "guest"}

print(get_admin_password())
print(get_admin_password.__name__)


## the right way to do it
import functools

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f"No way {user['username']}!"
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

user = {"username": "Karl", "access_level": "guest"}

print(get_admin_password())
print(get_admin_password.__name__)


## decorating function with parameters
print('\n')
def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f"No way {user['username']}!"
    return secure_function


@make_secure
def get_password(panel):
    if(panel == "admin"):
        return "1234"
    elif(panel == "billing"):
        return "super_secure_password"
    
user = {"username": "Karl", "access_level": "admin"}
print(get_password("billing"))

## decorators with parameters
print('\n')
def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user['access_level'] == access_level:
                return f"{access_level} permissions for {user['username']}: {func(*args, **kwargs)}"
            else:
                return f"No {access_level} permissions for {user['username']}!"
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("user")
def get_dashboard_password():
    return "user: user_password"

user = {"username": "Karl", "access_level": "admin"}
print(get_admin_password())
print(get_dashboard_password())

user = {"username": "Heinrich", "access_level": "user"}
print(get_admin_password())
print(get_dashboard_password())

user = {"username": "Jan", "access_level": "guest"}
print(get_admin_password())
print(get_dashboard_password())
