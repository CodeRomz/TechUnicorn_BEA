from pydantic import BaseModel, Field, EmailStr

class AppointmentBookSchema(BaseModel):
    _id: int = Field(default=None)
    doctor_id: int = Field(default=None)
    patient_id: int = Field(default=None)
    date: datetime = Field(default=None)
    start_time: str = Field(default=None)
    end_time: str = Field(default=None)
    status: str = Field(default=None)



