from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('AI-ML.html')

@app.route('/sidebar')
def sidebar():
    return render_template('sidebar.html')


@app.route('/FrontDesk')
def frontdesk():
    return render_template('FrontDesk.html')

@app.route('/DoorCam')
def cam():
    return render_template('DoorCam.html')

@app.route('/PersonalAssistant')
def assistant():
    return render_template('PersonalAssistant.html')

@app.route('/Health')
def health():
    return render_template('HealthPredict.html')

@app.route('/LaneDetection')
def lane():
    return render_template('LaneDetection.html')

@app.route('/SmartShopping')
def shop():
    return render_template('SmartShopping.html')

@app.route('/SuperRobotArm')
def robo():
    return render_template('SuperRobotArm.html')

@app.route('/AIFarming')
def farm():
    return render_template('AIFarming.html')

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')

if __name__ == '__main__':
    app.run(debug=True,host=('0.0.0.0'))
