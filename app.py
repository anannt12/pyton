from flask import Flask, render_template
import pyautogui
import time
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/executePythonScript')
def execute_python_script():
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'alt', 'del'); time.sleep(0.5)
    pyautogui.typewrite("https://www.youtube.com/@AllRounderAnannt?sub_confirmation=1")
    pyautogui.press('enter'); time.sleep(0.01)
    pyautogui.press('enter'); time.sleep(2)
    pyautogui.press(['tab', 'tab']); time.sleep(0.2)
    pyautogui.press('enter'); time.sleep(0.2)
    pyautogui.press('enter')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
