from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd

app = Flask(__name__)

# Sample product data (in a real application, this would come from a database)
product_data = {
    "apple": {"nutrition": "52 calories", "sustainability": "Low carbon footprint"},
    "banana": {"nutrition": "96 calories", "sustainability": "Moderate carbon footprint"}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/product', methods=['GET'])
def get_product_info():
    product_name = request.args.get('name').lower()
    if product_name in product_data:
        return jsonify(product_data[product_name])
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
    