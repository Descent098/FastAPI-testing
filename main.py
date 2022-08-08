# Standard library dependencies
from typing import List
from random import randint, choice

# Internal Dependencies
from models import User

# Third party dependencies
from fastapi import FastAPI, Request,Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Descent098 FastAPI Testing", 
    description="A demo app used to learn FastAPI", 
    host="0.0.0.0",
    debug=True
    )

users = [User()]
for index, _ in enumerate(range(randint(2,55))):
    users.append(User(name=choice(["Kieran", "Craig", "Roberio", "Liao"]), age=randint(18,75), country=choice(["Canada", "USA", "Brazil", "Taiwan"]), user_id=2+index))


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/user/{user_id}", response_model=User, name="Get user by ID")
async def get_user(user_id:int):
    """Gets users based on provided ID

    Parameters
    ----------
    user_id : int
        The id of the user to get
    """
    return vars(users[user_id-1])


@app.get("/fancy/user/{user_id}", response_class=HTMLResponse, name="Get user by ID with a nice frontend")
async def get_user_fancy(user_id:int, request:Request):
    """Get user by ID with a nice frontend

    Parameters
    ----------
    user_id : int
        The id of the user to get
    """
    gender = choice(["male", "female"])
    return templates.TemplateResponse("single_user.html", {"request": request,"app":app, "user":users[user_id-1], "gender":gender})

@app.get("/users", response_model=List[User], name="Get All users")
async def get_users():
    """Gets all users"""
    return [vars(user) for user in users]

@app.get("/user", response_class=RedirectResponse)
async def get_user_incorrect():
    """If someone forgets an ID they will be redirected to /"""
    return RedirectResponse("/")

@app.post("/user")
async def create_user(name:str = Form(example="kieran"), age:int = Form(example=23), country:str = Form(example="Canada")):
    """Used to create a new user"""
    user_id = len(users) + 1
    users.append(User(name=name, age=age, country=country, user_id=user_id))
    return RedirectResponse(f"/users/{user_id}", status_code=302)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """The default route that is a dashboard for the project"""
    # Can also pass a context dictionary
    return templates.TemplateResponse("index.html", {"request": request,"app":app, "users":users})

if __name__ == "__main__":
    from uvicorn.main import run # Used to start fastapi (ASGI proxy service)
    run(app="main:app", reload=True, debug=True) # Let's you skip using `uvicorn main:app --reload --debug`
    # run(app=app, host="0.0.0.0") # Let's you skip using `uvicorn main:app`
