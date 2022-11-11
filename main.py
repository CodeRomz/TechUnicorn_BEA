import uvicorn
from fastapi import FastAPI
from tubea_dbcon import TubeaDbExec
from tubea_jwt import signJWT


app = FastAPI()

# user registration and add the data in mongodb
@app.post("/register", tags=["Register User"])
def fa_register(user_id, user_name, user_password):
    register_user = TubeaDbExec("user")
    register_user.add_data(user_id, user_name, user_password)
    return {
        "data": "post added."
    }

@app.post("/user/login", tags=["user login"])
def fa_login(user, password):
    verify_user = TubeaDbExec("user")

    uv_value = verify_user.verify_login_data(user)
    try:
        if uv_value['user_name'] == None or uv_value["user_password"] == None:
            return {
                "error": "Wrong login details! none"
            }
        elif uv_value['user_name'] == user and uv_value["user_password"] == password:
            # return signJWT(user.email)
            return {
                "login": "success"
            }
        else:
            return {
                "error": "Wrong login details!"
            }
    except Exception as e:
        print(e)
        return {
            "error": "Wrong login details! exept"
        }


uvicorn.run(app, host="127.0.0.1", port=8000)


# register_user.add_data(2, "first username", "first password")

# print(register_user.view_data(2))


