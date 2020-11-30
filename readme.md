How to setup on your local machine.

- Clone the git repository anywhere on your system.  
- Install the [virtual environment](https://pythoncircle.com/post/404/virtual-environment-in-python-a-pocket-guide/)
- Activate the virtual environment using command `source path-to-venv-folder/bin/activate`
- CD to the folder where code was placed from git repository.
- Install all the dependencies using command `pip install -r requirements.txt`
- Start the web-app on any empty port using command `python manage.py runserver 8888` where 8888 is the port.
- Open browser and go to localhost:8888
- Upload any text file containing and image will be displayed.