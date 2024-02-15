import xml.etree.ElementTree as ET
from flask import Flask, jsonify

tree = ET.parse("seeds.xml")
root = tree.getroot()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to rust crossbreed API"


@app.route('/hello', methods=['GET'])
def hello():
    return "hello"

@app.route('/add', methods=['PUT'])
def add():
    new_seed = ET.SubElement(root, "Seed")
    new_seed.set("genes", "XXXXXX")
    tree.write("seeds.xml")

if __name__ == '__main__':
    app.run(debug=True)