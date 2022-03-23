from app.app import app

import threading


def csv_task():
    csv_thread = threading.Thread(target=invoke_via_subprocess)
    csv_thread.start()


def invoke_via_subprocess():
    from app.csv_task.helpers.csv_generator import CsvGenerator
    CsvGenerator().main()


""" run csv task """
csv_task()


# app.run("localhost", 5000, use_reloader=True)