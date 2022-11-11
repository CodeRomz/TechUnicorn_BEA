import uvicorn
from fastapi import FastAPI
from tubea_dbcon import TubeaDbExec


app = FastAPI()

# user registration and add the data in mongodb
@app.post("/register", tags=["Register"])
def fa_register(user_id, user_name, user_password, user_access):
    register_user = TubeaDbExec("user")
    register_user.add_user_data(user_id, user_name, user_password, user_access)
    return {
        "data": "post added."
    }

@app.post("/user/login", tags=["Login"])
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


@app.get("/appointments", tags=["Appointment"])
def fa_view_appointment():
    view_appointmnet = TubeaDbExec("appointment")

    for data in view_appointmnet.view_all_data():
        print(data)


    return view_appointmnet.view_all_data()

@app.get("/doctors", tags=["Doctors"])
def fa_view_doctors():
    view_doctor = TubeaDbExec("user")

    for data in view_doctor.view_all_access("doctor"):
        print(data)


    return view_doctor.view_all_access("doctor")

@app.get("/doctors/{doctor_id}", tags=["Doctors"])
def fa_view_doctors_information(doctor_id):
    view_doctor_user = TubeaDbExec("user")
    view_doctor_appointments = TubeaDbExec("appointment")

    doctor_user_info = view_doctor_user.view_byUser_byAccess(doctor_id, "doctor")

    doctor_appointment_details = view_doctor_appointments.view_appointment_byDoctorId(doctor_id)

    doctor_information = doctor_user_info + doctor_appointment_details

    return doctor_information






@app.get("/book_appointment", tags=["Appointment"])
def fa_book_appointment(appointment_id, doctor_id, patient_id, date, start_time, end_time, status):
    book_appointment = TubeaDbExec("appointment")

    book_appointment.book_appointment(appointment_id, doctor_id, patient_id, date, start_time, end_time, status)
    return {
        "data": "appointment added."
    }

uvicorn.run(app, host="127.0.0.1", port=8000)


# register_user.add_data(2, "first username", "first password")

# print(register_user.view_data(2))


