from bottle import route, run
import time

@route('/')
def hello():
    html = "The current time is: " + str(time.asctime()) + "\n"
    return html

run(host='0.0.0.0', port=8080, debug=True)
