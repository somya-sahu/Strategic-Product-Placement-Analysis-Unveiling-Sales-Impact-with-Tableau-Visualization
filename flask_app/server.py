import csv
import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

class DataManager:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = self.load_data()
    
    def load_data(self):
        rows = []
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    rows.append(row)
        return rows
    
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

class RequestHandler(BaseHTTPRequestHandler):
    data_manager = None
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    def do_GET(self):
        path = urlparse(self.path).path
        
        if path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_home_page().encode())
        
        elif path == '/visualizations':
            try:
                with open(os.path.join(self.base_dir, 'templates/visualizations.html'), 'r') as f:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(f.read().encode())
            except Exception as e:
                self.send_error(404)
        
        elif path == '/dashboard':
            try:
                with open(os.path.join(self.base_dir, 'templates/dashboard.html'), 'r') as f:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(f.read().encode())
            except:
                self.send_error(404)
        
        elif path == '/story':
            try:
                with open(os.path.join(self.base_dir, 'templates/story.html'), 'r') as f:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(f.read().encode())
            except:
                self.send_error(404)
        
        elif path == '/api/summary':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.data_manager.get_summary()).encode())
        
        elif path == '/api/top-products':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.data_manager.get_top_products()).encode())
        
        else:
            self.send_error(404)
    
    def get_home_page(self):
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Strategic Product Placement Analysis</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #f5f5f5; color: #333; }
        .navbar { background: #2c3e50; color: white; padding: 1rem; }
        .navbar h1 { margin-bottom: 0.5rem; }
        .nav-links { list-style: none; display: flex; gap: 2rem; flex-wrap: wrap; }
        .nav-links a { color: white; text-decoration: none; }
        .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
        .hero { text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 8px; margin: 2rem 0; }
        .summary-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 2rem 0; }
        .card { background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center; }
        .card h3 { color: #2c3e50; margin-bottom: 1rem; font-size: 0.9rem; text-transform: uppercase; }
        .card p { font-size: 1.8rem; color: #3498db; font-weight: bold; }
        table { width: 100%; border-collapse: collapse; background: white; margin-top: 1rem; }
        table thead { background: #34495e; color: white; }
        table th, table td { padding: 1rem; text-align: left; }
        table tbody tr:hover { background: #f8f9fa; }
        table td { border-bottom: 1px solid #ecf0f1; }
    </style>
</head>
<body>
    <nav class="navbar">
        <h1>Strategic Product Placement Analysis</h1>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            <li><a href="/visualizations">Visualizations</a></li>
            <li><a href="/dashboard">Dashboard</a></li>
            <li><a href="/story">Story</a></li>
        </ul>
    </nav>
    <div class="container">
        <section class="hero">
            <h2>Unveiling Sales Impact with Tableau Visualization</h2>
            <p>Analyze product positioning strategies and their impact on sales performance</p>
        </section>
        <section class="summary-cards">
            <div class="card">
                <h3>Total Products</h3>
                <p id="total-products">-</p>
            </div>
            <div class="card">
                <h3>Avg Sales Growth</h3>
                <p id="avg-sales-growth">-</p>
            </div>
            <div class="card">
                <h3>Avg Revenue Growth</h3>
                <p id="avg-revenue-growth">-</p>
            </div>
            <div class="card">
                <h3>Total Revenue Increase</h3>
                <p id="total-revenue">-</p>
            </div>
        </section>
        <section>
            <h3>Top 10 Performing Products</h3>
            <table id="products-table">
                <thead>
                    <tr>
                        <th>Product Name</th>
                        <th>Category</th>
                        <th>Sales Growth %</th>
                        <th>Revenue Growth %</th>
                    </tr>
                </thead>
                <tbody></tbody>
            </table>
        </section>
    </div>
    <script>
        async function loadSummary() {
            const response = await fetch('/api/summary');
            const data = await response.json();
            document.getElementById('total-products').textContent = data.total_products;
            document.getElementById('avg-sales-growth').textContent = data.avg_sales_growth.toFixed(2) + '%';
            document.getElementById('avg-revenue-growth').textContent = data.avg_revenue_growth.toFixed(2) + '%';
            document.getElementById('total-revenue').textContent = '$' + data.total_revenue_increase.toLocaleString('en-US', {maximumFractionDigits: 0});
        }
        async function loadTopProducts() {
            const response = await fetch('/api/top-products');
            const products = await response.json();
            const tbody = document.querySelector('#products-table tbody');
            tbody.innerHTML = '';
            products.forEach(product => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${product.Product_Name}</td>
                    <td>${product.Category}</td>
                    <td>${product.Sales_Growth_Percent.toFixed(2)}%</td>
                    <td>${product.Revenue_Growth_Percent.toFixed(2)}%</td>
                `;
                tbody.appendChild(row);
            });
        }
        document.addEventListener('DOMContentLoaded', function() {
            loadSummary();
            loadTopProducts();
        });
    </script>
</body>
</html>'''
    
    def log_message(self, format, *args):
        pass

def run_server(port=5000):
    data_path = os.path.join(os.path.dirname(__file__), '../data/prepared_data.csv')
    RequestHandler.data_manager = DataManager(data_path)
    
    server = HTTPServer(('0.0.0.0', port), RequestHandler)
    print(f"Server running on http://localhost:{port}")
    print("Routes:")
    print("  / - Home page")
    print("  /visualizations - Data visualizations (Pie, Bar, Line, Scatter, Doughnut, Radar charts)")
    print("  /dashboard - Dashboard")
    print("  /story - Story")
    print("  /api/summary - API summary")
    print("  /api/top-products - API top products")
    server.serve_forever()

if __name__ == '__main__':
    run_server()
