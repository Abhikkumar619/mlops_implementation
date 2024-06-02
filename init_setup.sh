echo [$(date)]: "START"


echo [$(date)]: "Creating mlop_env with python 3.8 version"

conda create -p mlop_env python=3.8 -y

echo [$(date)]: "Activating the conda"

conda activate ./mlop_env/

echo [$(echo)]: "Install the dependency require for project"

pip install -r requirements.txt

echo [$(date)]: "End"

