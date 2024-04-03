Playground for different python libraries, techniques, and notebooks

# Set Up for my own libraries
1. Set up virtual environment with `virtualenv venv` and activate it `source venv/bin/activate`
  a. Note: Windows commands are slightly different
2. In the virtual environment shell, run `pip install -r requirements.txt`
3. To add newly installed libraries to requirements.txt, can fun `pip freeze > requirements.txt` after installation

# Can also just use the anaconda distribution to run everything
### Option 1:
1. Set up environment with `conda create --name myenv python=3.12`
  a. Can be whatever python environment I want
2. Activate environment with `conda activate myenv`
### Option 2:
1. Select Python interpreter as anaconda