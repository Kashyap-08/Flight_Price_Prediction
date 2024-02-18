# Initialze Git and Git Push Commands

* Step1: Create Folder  
* Step2:  
    * Initialize Git Repo by using Command `git init` in command prompt.
    * You can push changes by using below commands:
        * `git add .`
        * `git status` 
        * `git commit -m "Enter you comment"`
        * `git push origin master`

# Create Licence file in Git UI
* `Create new file` using  `Add file` dropdown box.
* Type `Licence` as the name of the file you want to create.
* you will get a new Option named `Choose a Licence Template`.
* Click on the option and you will get the list of Licence Templates.
* Choose the Template as per your Convenience.
* Once Choosen, you can commit the changes in `master` branch.

# Create  and .gitignore file in Git UI
* `Create new file` using  `Add file` dropdown box.
* Type `.gitignore` and you will get the dropdown box below named  `Chooose .gitignore template`.
* Type `python` and select the option that suggest.
* You will get the template of `.gitignore` file.
* Commit the changes in Master branch.

# Create template.py file that create a Framework of the Project
* Run template.py file using command `python template.py`.
* It will create all the files and folders that is required for Industry ready project.
* It is also called as Boiler Plate code, that is universal for any Data Science Project.

# Create Virtual Environment
* Mention all the required Library in `requirements.txt` file that you want to install.
* Write a bash code to automatically create Virtiual environment in `init_step.py` file.
* `init_steup.py` file will create a virtual env using python, it will activate the env and will install all the required libraries mentioned in `requirements.txt` file.
* Run the Command `bash init_setup.sh` in git bash to run the setup file.
* it will create virtual env, activate the venv and will install all the requied packages.

# Create a Local Package
* Create file named `setup.py` and write code to create a package.
* To install the Local Package add `-e .` in `requirements.txt` file, or you can install package using `python setup.py install`
* rerun install the package using command `bash init_setup.sh`
