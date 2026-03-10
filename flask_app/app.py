from flask import Flask, render_template, jsonify
import csv
import os
from statistics import mean

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'prepared_data.csv')

def read_csv_data():
    """Read CSV file and return list of dicts"""
    data = []
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/visualizations")
def visualizations():
    return render_template("visualizations.html")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/api/summary')
def get_summary():
    try:
        data = read_csv_data()
        if not data:
            return jsonify({'error': 'No data found'}), 500
        
        products = set(row.get('Product_ID', '') for row in data)
        categories = set(row.get('Category', '') for row in data)
        sales_growth = [float(row.get('Sales_Growth_Percent', 0)) for row in data if row.get('Sales_Growth_Percent')]
        revenue_growth = [float(row.get('Revenue_Growth_Percent', 0)) for row in data if row.get('Revenue_Growth_Percent')]
        revenue_increase = [float(row.get('Revenue_Increase', 0)) for row in data if row.get('Revenue_Increase')]
        effectiveness = [float(row.get('Effectiveness_Score', 0)) for row in data if row.get('Effectiveness_Score')]
        
        summary = {
            'total_products': len(products),
            'total_categories': len(categories),
            'avg_sales_growth': round(mean(sales_growth), 2) if sales_growth else 0,
            'avg_revenue_growth': round(mean(revenue_growth), 2) if revenue_growth else 0,
            'total_revenue_increase': round(sum(revenue_increase), 2) if revenue_increase else 0,
            'avg_effectiveness': round(mean(effectiveness), 2) if effectiveness else 0
        }
        return jsonify(summary)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/top-products')
def get_top_products():
    try:
        data = read_csv_data()
        if not data:
            return jsonify({'error': 'No data found'}), 500
        
        for row in data:
            row['Sales_Growth_Percent'] = float(row.get('Sales_Growth_Percent', 0))
        
        sorted_data = sorted(data, key=lambda x: x['Sales_Growth_Percent'], reverse=True)[:10]
        top_products = [
            {
                'Product_Name': row.get('Product_Name', ''),
                'Category': row.get('Category', ''),
                'Sales_Growth_Percent': row.get('Sales_Growth_Percent', 0),
                'Revenue_Growth_Percent': float(row.get('Revenue_Growth_Percent', 0))
            }
            for row in sorted_data
        ]
        return jsonify(top_products)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
