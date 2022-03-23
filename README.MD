# BARRICK TASK FOR FOX INTEGRATION #

### CSV TASK ###

CSV task can either run/debug file run_csv_task.py or input $ flask run and visit http://127.0.0.1:5000/ 

### FILE TASK ###

File task can either run command $ gunicorn --bind 0.0.0.0:5000 --workers 6 "app.app:create_app()" or dock compose up

As the task should not be hosted on any cloud server, I was trying to use gunicorn to solve the multiple request 
requirement.

As no file id should be used in this task, I just use a cursor to mark the order.