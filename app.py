from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/distance_plot')
def distance_plot():
    return render_template('distance_plot.html')

@app.route('/error_plot')
def error_plot():
    return render_template('error_plot.html')

@app.route('/range_plot')
def range_plot():
    return render_template('range_plot.html')

@app.route('/soc_plot')
def soc_plot():
    return render_template('soc_plot.html')

@app.route('/temp_plot')
def temp_plot():
    return render_template('temp_plot.html')

@app.route('/voltage_plot')
def voltage_plot():
    return render_template('voltage_plot.html')

if __name__ == '__main__':
    app.run(debug=True)
