from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Configuration
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'prepared_data.csv')

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')



@app.route("/visualizations")
def visualizations():
    return render_template("visualizations.html")




@app.route('/dashboard')
def dashboard():
    """Tableau dashboard page"""
    return render_template('dashboard.html')

@app.route('/story')
def story():
    """Tableau story page"""
    return render_template('story.html')
# API Endpoints
@app.route('/api/summary')
def get_summary():
    """API endpoint for summary statistics"""
    try:
        df = pd.read_csv(DATA_PATH)
        summary = {
            'total_products': int(df['Product_ID'].nunique()),
            'total_categories': int(df['Category'].nunique()),
            'avg_sales_growth': float(df['Sales_Growth_Percent'].mean()),
            'avg_revenue_growth': float(df['Revenue_Growth_Percent'].mean()),
            'total_revenue_increase': float(df['Revenue_Increase'].sum()),
            'avg_effectiveness': float(df['Effectiveness_Score'].mean())
        }
        return jsonify(summary)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/top-products')
def get_top_products():
    """API endpoint for top performing products"""
    try:
        df = pd.read_csv(DATA_PATH)
        top_products = df.nlargest(10, 'Sales_Growth_Percent')[
            ['Product_Name', 'Category', 'Sales_Growth_Percent', 'Revenue_Growth_Percent']
        ].to_dict('records')
        return jsonify(top_products)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
