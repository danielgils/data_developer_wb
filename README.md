# Req21560 – Extended Term Consultant – Data Developer – Practical Test

This repo has three different files corresponding to *Section I* and *II* of this practical test.
To run the files of the *Section I* follow these steps:
1. Clone this repo in your local computer.
1. Make sure you have installed Python 3.10.6 or a later version. If you don't have it or have a different version, you can use `pyenv` to manage different python versions in the same machine (see [here](https://realpython.com/intro-to-pyenv/)).
1. Create a virtual environment using `venv`. You can run in the terminal the following `python3 -m venv venv` where the second `venv` corresponds to the name of the virtual enviroment.
1. Activate the virtual environment. In unix based OS you can run in the terminal `source venv/bin/activate`. In Windows you can run in powershell or CMD `.\venv\Scripts\activate`.
1. Install the required libraries. You can run in the terminal `pip install -r requirements.txt`. 

Once this process is done, you can do the following:
- Section I
    - API: This is an API developed with FastAPI to list the entries in the Titanic file. To see the API working locally you can run in the terminal `uvicorn api:app --reload --host 0.0.0.0`. This API has two endpoints:
        - `http://0.0.0.0:8000/titanic` shows all the entries in the titanic file
        - `http://0.0.0.0:8000/titanic/{id}` shows the information of the passenger based on his/her `PassengerID`.
        - The documentation of the API can be seen at `http://0.0.0.0:8000/docs`
    - Parsing: This file contain three different attempts to parse correctly the information contained in the JSON file. The resulting dataframes are saved inside the `parsed_json` folder. The second option is good enough for most cases but for `industry_codes` variable which contain a list of codes. In the case that these codes are needed, then the third option may work. It is important to note that the JSON file cannot be imported directly because it has single quotes instead of doubles, so in the code these quotes are changed.

This test was developed in Ubuntu Server 22.04.1 LTS, using Python 3.10.6 with the help of ChatGPT.