
from datetime import datetime

import pandas as pd
import uvicorn
from fastapi import FastAPI
from tubea_dbcon import TubeaDbExec


app = FastAPI()

# user registration and add the data in mongodb
@app.post("/register", tags=["Register"], description='User registration')
def fa_register(user_id, user_name, user_password, user_access):
    register_user = TubeaDbExec("user")
    register_user.add_user_data(user_id, user_name, user_password, user_access)
    return {
        "data": "post added."
    }

@app.post("/user/login", tags=["Login"], description='User Login')
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


@app.get("/appointments", tags=["Appointment"], description='View all appointments')
def fa_view_appointment():
    view_appointmnet = TubeaDbExec("appointment")

    for data in view_appointmnet.view_all_data():
        print(data)


    return view_appointmnet.view_all_data()

@app.get("/doctors", tags=["Doctors"], description='list of doctors')
def fa_view_doctors():
    view_doctor = TubeaDbExec("user")

    for data in view_doctor.view_all_access("doctor"):
        print(data)


    return view_doctor.view_all_access("doctor")

@app.get("/doctors/{doctor_id}", tags=["Doctors"], description='doctor details')
def fa_view_doctors_information(doctor_id):
    view_doctor_user = TubeaDbExec("user")
    view_doctor_appointments = TubeaDbExec("appointment")

    doctor_user_info = view_doctor_user.view_byUser_byAccess(doctor_id, "doctor")

    doctor_appointment_details = view_doctor_appointments.view_appointment_byDoctorId(doctor_id)

    output = pd.DataFrame()

    for details in doctor_appointment_details:
        df_dictionary = pd.DataFrame([details])
        output = pd.concat([output, df_dictionary], ignore_index=True)

    # print(output.head())
    print(output)


    # df = pd.DataFrame(doctor_appointment_details)
    #
    # df2 = output.pivot(index='doctor_id', columns='date', values='status')

    # print(df2.head())
    print('\n Pivot \n')
    try:
        output.pivot_table(index='running_time', columns='date')
        print(output)
    except Exception as e:
        print(e)

    return doctor_appointment_details







@app.get("/book_appointment", tags=["Appointment"], description='Book an appointment')
def fa_book_appointment(appointment_id, doctor_id, patient_id, date, start_time, end_time, status):

    book_appointment = TubeaDbExec("appointment")

    timeFormat = '%H:%M:%S'

    s_time = datetime.strptime(start_time, timeFormat)
    e_time = datetime.strptime(end_time, timeFormat)

    running_time = e_time - s_time

    max_time = datetime.strptime('2:00:00', timeFormat)
    max_time_compare = datetime.strptime('00:00:00', timeFormat)

    min_time = datetime.strptime('00:15:00', timeFormat)
    min_time_compare = datetime.strptime('00:00:00', timeFormat)

    max_timeCompare = max_time - max_time_compare

    min_timeCompare = min_time - min_time_compare

    print(running_time)
    print(max_timeCompare)
    print(min_timeCompare)

        #Time checking (Minimum Duration is 15 min, Max duration 2hrs)
    if running_time <= max_timeCompare and running_time >= min_timeCompare:
        book_appointment.book_appointment(appointment_id, doctor_id, patient_id, date, start_time, end_time, str(running_time), status)
        return {
            "data": "appointment added.",
            "reminder": "Be at the doctor's clinic 5 minutes before the scheduled appointment time"
        }
    else:
        return {
            "Time Error": "Kindly check the start time and End time Minimum Duration is 15 min, Max duration 2hrs",
            "reminder": "Be at the doctor's clinic 5 minutes before the scheduled appointment time"
        }


uvicorn.run(app, host="127.0.0.1", port=8000)



