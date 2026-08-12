from fastapi import FastAPI


from agents.tutor_agent import TutorAgent
from agents.correction_agent import CorrectionAgent


from database import engine
from models import Base



Base.metadata.create_all(
    bind=engine
)


app=FastAPI(
    title="LinguaMentor AI"
)



@app.get("/")
def home():

    return {
        "message":
        "LinguaMentor AI running"
    }



@app.post("/chat")
def chat(data:dict):


    tutor=TutorAgent(

        data["target_language"],

        data["native_language"],

        data["level"],

        data["interests"]

    )


    answer=tutor.chat(
        data["message"]
    )


    correction=CorrectionAgent().analyze(

        data["message"],

        data["target_language"]

    )


    return {

        "reply":answer,

        "red_pen":correction

    }