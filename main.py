import uvicorn
from fastapi import FastAPI
from tubea_dbcon import TubeaDbExec


app = FastAPI()

# user registration and add the data in mongodb
@app.post("/register", tags=["Register User"])
def fa_register(user_id, user_name, user_password):
    register_user = TubeaDbExec("user")
    register_user.add_data(user_id, user_name, user_password)
    return {
        "data": "post added."
    }





uvicorn.run(app, host="127.0.0.1", port=8000)


# register_user.add_data(2, "first username", "first password")

# print(register_user.view_data(2))


