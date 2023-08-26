from flask import Flask, render_template
import json

app = Flask(__name__)

with open('output.json', 'r', encoding='utf-8') as json_file:
    plugins = json.load(json_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plugins')
def plugin_list():
    return render_template('allpluginspage.html', plgnlist=plugins)

@app.route('/plugin-details/<string:plugin_id>')
def plugin_details(plugin_id):
    plgn = next((e for e in plugins if e['id'] == plugin_id), None)
    if plgn:
        return render_template('plugin_details.html', item=plgn)
    return "Plugin details are not found."

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
