from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from models import App
from database import session_house

class insert_base(BaseModel):
    some_notes:str

app=FastAPI()

@app.post("/paste")
def paste_something(some_pastes:insert_base):
    db=session_house()
    new_paste=App(pastes=some_pastes.some_notes)
    db.add(new_paste)
    db.commit()
    db.close()
    return {"message": "Paste saved successfully"}

@app.get("/paste")
def read_paste():
    db=session_house()
    all_data=db.query(App).all()
    db.close()
    return {"message":all_data}

@app.get("/paste/{paste_id}")
def specific_paste(paste_id:int):
    db=session_house()
    idiot=db.query(App).filter(App.id==paste_id).first()
    #length=db.query(App).count() //gonna use later in frontend
    db.close()
    return{"message":idiot}






