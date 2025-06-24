This is a placeholder file to keep the VirtualEnv folder inside of the Template folder for GitHub.

This would be the folder where your virtual environment would be, the usual names for the virtual environment folder are: Venv, or MyVenv.

You don't actually create this folder by typing: 'mkdir ....'

If you want to create a virtual environment here is the command:

**Git Bash / Bash / Linux / macOS Terminal:**
- `python3 -m venv MyVenv`
or
- `python -m venv MyVenv`

To activate virtual env: `source MyVenv/bin/activate`

**Windows Powershell:**
- `python -m venv MyVenv`

To activate virtual env: `.\MyVenv\Scripts\Activate.ps1`

**Windows CMD:**
- `python -m venv MyVenv`

To activate virtual env: `MyVenv\Scripts\activate.bat`

**To deactivate virtual environments type and enter: `deactivate`**

**What do the commands do?**
- The keyword 'python'/'python3' just calls the Python interpreter (some systems like macOS require python3 to specifically refer to python 3.x...). On Windows, `python` typically points to the latest version installed.
- The keyword '-m' tells Python to run a 'module' as a script, in this case it runs the `venv` module. The '-' prefix is a flag/option, and the 'm' specifies the option to be 'module'.
- The keyword 'venv' is the standard Python module used to create lightweight virtual environments. So together: `-m venv` means "run the venv module as if it were a script".
- The word 'MyVenv' is **NOT** a keyword, that's just a name I gave to the folder where the virtual environment will be created. You can change it to any name you want, just try to make it, make sense.

The command to **activate**:
- After creating a virtual environment, **activating it** sets your shell to use the Python interpreter and libraries from the virtual environment folder, instead of the global system Python.
- This makes sure that your project uses only the dependencies you installed in that environment.
- The keyword 'source' runs the `activate` shell script that sets environment variables for your terminal shell. Similiarly the Windows Powershell's command runs the Powershell version of the activate script from the environment.
- The big difference you'll see is that Git Bash/Linux/macOS has something called `bin` inside of the virtual environment folder, and Windows will have `Scripts`. These two, are just folders, and inside of these two folders you'll find a file either called `activate` or `Activate`, depending on the system you're using. You're essentially calling that activate file in order to activate your virtual environment.

Now most of you are probably wondering why we should even use a virtual environment.

Creating a virtual environment helps isolate dependencies (i.e. packages/libraries) so that packages installed for one project don't interfere with others.

It ensures consistency and prevents version conflicts, especially when collaborating (and others cloning and running the app) and deploying.

## **Once your project is running and you have some packages installed**

After installing all necessary packages inside of your virtual environment, you should freeze them using this command:

- `pip freeze > requirements.txt`

This will generate a `requirements.txt` file listing all installed packages (we already have it in the template, so it'll just overwrite it).

Having this `requirements.txt` file makes it easy to replicate the app's environment elsewhere (on a new machine, or for new users, or new teammates), to do all the required installations (packages/libraries) run this command:

- `pip install -r requirements.txt`

**Going over the freeze command:**

- `pip freeze`: Outputs a list of all installed packages and their exact versions (e.g., `Flask==2.3.2`).
- `>`: This is a **redirection operator**. It tells the shell to send the output into a file instead of displaying it on the screen.
- `requirements.txt`: The file where your environment’s package list is saved. If it doesn’t exist, it will be created; if it does, it will be overwritten.

**Going over the install -r requirements.txt command:**

This `requirements.txt` file is essential for sharing your project or deploying it. Others can recreate your environment using:
- `pip install -r requirements.txt`

All this command does, is tells python to install all of the libraries it 'reads' from the requirements.txt file.