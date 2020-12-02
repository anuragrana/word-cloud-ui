![word cloud image](wordcloud.png)


This single page Django web application lets you upload the text or docx file and generates the word cloud image from the text content in uploaded file.  




#### How to setup on your local machine.

- Clone the git repository anywhere on your system.  
- Install the [virtual environment](https://pythoncircle.com/post/404/virtual-environment-in-python-a-pocket-guide/)
- Activate the virtual environment using command `source path-to-venv-folder/bin/activate`
- CD to the folder where code was placed from git repository.
- Install all the dependencies using command `pip install -r requirements.txt`
- Start the web-app on any empty port using command `python manage.py runserver 8888` where 8888 is the port.
- Open browser and go to localhost:8888
- Upload any text file containing and image will be displayed.

---
##### References:
How to setup Python, pip and virtual environment on Windows 10:   
https://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/

Install pip on windows machine:  
https://stackoverflow.com/questions/4750806/how-can-i-install-pip-on-windows

 
If exception module not found error due to docx module:  
https://stackoverflow.com/questions/22765313/when-import-docx-in-python3-3-i-have-error-importerror-no-module-named-excepti
