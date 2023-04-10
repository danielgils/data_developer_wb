# Req21560 – Extended Term Consultant – Data Developer – Practical Test

This repo has three different files corresponding to *Section I* and *II* of this practical test.

## Setup
To run the files of the *Section I* follow these steps:
1. Clone this repo in your local computer.
1. Make sure you have installed Python 3.10.6 or a later version. If you don't have it or have a different version, you can use `pyenv` to manage different python versions in the same machine (see [here for Unix based OS](https://realpython.com/intro-to-pyenv/), or [here for Windows](https://github.com/pyenv-win/pyenv-win)). Preferably, use `pyenv local 3.10.6` inside the folder of this repo, to assign this version to the folder.
1. Create a virtual environment using `venv`. You can run in the terminal the following `python3 -m venv venv` where the second `venv` corresponds to the name of the virtual enviroment.
1. Activate the virtual environment. In Unix based OS you can run in the Terminal `source venv/bin/activate`. In Windows you can run in Powershell `.\venv\Scripts\activate`.
1. Install the required libraries. In Unix based OS you can run in the Terminal `pip install -r requirements.txt`. In Windows you can run in Powershell `pip install -r requirements_windows.txt`. 

## Answers to the test
Once the setup is done, you can do the following:
- Section I
    - API: This is an API developed with FastAPI to list the entries in the Titanic file. The code is in the file `api.py`. 
        - To see the API working locally you can run in the Terminal/Powershell `uvicorn api:app --reload --host 0.0.0.0`. 
        - This API has three endpoints:
            - `http://0.0.0.0:8000/titanic` shows all the entries in the titanic file. This also works in `http://localhost:8000/titanic`.
            - `http://0.0.0.0:8000/titanic/{id}` shows the information of the passenger based on his/her `PassengerID`. This also works in `http://localhost:8000/titanic/{id}`.
            - `http://0.0.0.0:8000/titanic/?` shows the information of the passenger based on his/her features. This endpoint has query parameters to filter based on multiple features, i.e., the filter need to be in the url. For example, `http://0.0.0.0:8000/titanic/?sex=female&pclass=3` shows only females passengers in third class. This also works in `http://localhost:8000/titanic/?sex=female&pclass=3`.
        - The documentation of the API can be seen at `http://0.0.0.0:8000/docs`. This also works in `http://localhost:8000/docs`.
    - Parsing: The code is in the file `parsing.py`and to run it type in the Terminal/Powershell `python parsing.py`. 
        - The dataframes resulting of this script are saved inside the `parsed_json` folder. 
        - This file contains three different attempts to parse correctly the information contained in the JSON file: 
            - The first attempt consists in directly transform the JSON file into a dataframe using Pandas (does not work great). 
            - The second attempt consists in using `json_normalize` function, which results are good enough for most cases but for `industry_codes` variable which contain a list of codes. 
            - In the case that these codes are needed, then the third option may work. 
        - It is important to note that the JSON file cannot be imported directly because it has single quotes instead of doubles, so in the code these quotes are changed.
- Section II: The answers are in the file `section2.txt`.

## Notes
- This practical test was developed using Python 3.10.6 in VS Code on Ubuntu Server 22.04.1 LTS, with the help of ChatGPT.
- The code was tested in macOS Monterrey (v12.5) using `pyenv local 3.10.6`.
- The code was tested in Windows 10 using `pyenv local 3.10.6`.
- `uvloop` package is not available in Windows, and this package was installed as a dependency of another package in Ubuntu. This is why there are two different `requirements` files.