from tubea_dbcon import TubeaDbExec

verify_user = TubeaDbExec("user")

uv_value = verify_user.verify_login_data("third name")

print(uv_value['user_password'])