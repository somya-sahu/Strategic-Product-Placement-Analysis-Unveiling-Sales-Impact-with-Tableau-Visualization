import csv
import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime

class DataCollection:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = []
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r') as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
        return self.data
    
    def get_summary(self):
        if not self.data:
            return {}
        sales_growth = [float(r.get('Sales_Growth_Percent', 0)) for r in self.data]
        revenue_growth = [float(r.get('Revenue_Growth_Percent', 0)) for r in self.data]
        revenue_increase = [float(r.get('Revenue_Increase', 0)) for r in self.data]
        return {
            'total_products': len(self.data),
            'total_categories': len(set(r.get('Category', '') for r in self.data)),
            'avg_sales_growth': round(sum(sales_growth) / len(sales_growth), 2),
            'avg_revenue_growth': round(sum(revenue_growth) / len(revenue_growth), 2),
            'total_revenue_increase': round(sum(revenue_increase), 2)
        }
    
    def get_categorical_analysis(self):
        categorical_fields = ['Category', 'Region', 'Media_Type', 'Consumer_Age_Group']
        analysis = {}
        for field in categorical_fields:
            categories = {}
            for row in self.data:
                value = row.get(field, 'Unknown')
                categories[value] = categories.get(value, 0) + 1
            analysis[field] = categories
        return analysis
    
    def get_top_products(self, limit=10):
        sorted_data = sorted(self.data, key=lambda x: float(x.get('Sales_Growth_Percent', 0)), reverse=True)
        return [
            {
                'Product_Name': r.get('Product_Name', ''),
                'Category': r.get('Category', ''),
                'Sales_Growth_Percent': float(r.get('Sales_Growth_Percent', 0)),
                'Revenue_Growth_Percent': float(r.get('Revenue_Growth_Percent', 0))
            }
            for r in sorted_data[:limit]
        ]
    
    def get_insights(self):
        if not self.data:
            return {}
        sales_growth = [float(r.get('Sales_Growth_Percent', 0)) for r in self.data]
        categories = {}
        for row in self.data:
            cat = row.get('Category', 'Unknown')
            growth = float(row.get('Sales_Growth_Percent', 0))
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(growth)
        return {
            'avg_sales_growth': round(sum(sales_growth) / len(sales_growth), 2),
            'max_sales_growth': round(max(sales_growth), 2),
            'min_sales_growth': round(min(sales_growth), 2),
            'category_performance': {cat: round(sum(vals) / len(vals), 2) for cat, vals in categories.items()}
        }

class RequestHandler(BaseHTTPRequestHandler):
    collector = None
    
    def do_GET(self):
        path = urlparse(self.path).path
        
        if path == '/api/data-collection/summary':
            self.send_json(self.collector.get_summary())
        elif path == '/api/data-collection/categorical':
            self.send_json(self.collector.get_categorical_analysis())
        elif path == '/api/data-collection/top-products':
            self.send_json(self.collector.get_top_products())
        elif path == '/api/data-collection/insights':
            self.send_json(self.collector.get_insights())
        elif path == '/api/data-collection/all':
            self.send_json({
                'summary': self.collector.get_summary(),
                'categorical': self.collector.get_categorical_analysis(),
                'top_products': self.collector.get_top_products(),
                'insights': self.collector.get_insights(),
                'timestamp': datetime.now().isoformat()
            })
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Not Found'}).encode())
    
    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def log_message(self, format, *args):
        pass

def run_server(port=5001):
    data_path = os.path.join(os.path.dirname(__file__), '../data/prepared_data.csv')
    RequestHandler.collector = DataCollection(data_path)
    
    server = HTTPServer(('0.0.0.0', port), RequestHandler)
    print(f"Data Collection API running on http://localhost:{port}")
    print("Endpoints:")
    print("  /api/data-collection/summary")
    print("  /api/data-collection/categorical")
    print("  /api/data-collection/top-products")
    print("  /api/data-collection/insights")
    print("  /api/data-collection/all")
    server.serve_forever()

if __name__ == '__main__':
    run_server()
