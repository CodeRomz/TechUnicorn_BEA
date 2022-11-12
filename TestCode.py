from tubea_dbcon import TubeaDbExec

view_doctor_user = TubeaDbExec("user")
view_doctor_appointments = TubeaDbExec("appointment")


doctor_id = 4

doctor_user_info = view_doctor_user.view_byUser_byAccess(int(doctor_id), "doctor")

doctor_appointment_details = view_doctor_appointments.view_appointment_byDoctorId(int(doctor_id))

for details in doctor_appointment_details:
    print(details)


print(doctor_user_info)