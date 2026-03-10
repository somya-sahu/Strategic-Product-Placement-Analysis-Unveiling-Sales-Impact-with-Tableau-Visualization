// Fetch and display summary statistics
async function loadSummary() {
    try {
        const response = await fetch('/api/summary');
        const data = await response.json();
        
        document.getElementById('total-products').textContent = data.total_products;
        document.getElementById('avg-sales-growth').textContent = data.avg_sales_growth.toFixed(2) + '%';
        document.getElementById('avg-revenue-growth').textContent = data.avg_revenue_growth.toFixed(2) + '%';
        document.getElementById('total-revenue').textContent = '$' + data.total_revenue_increase.toLocaleString('en-US', {maximumFractionDigits: 0});
    } catch (error) {
        console.error('Error loading summary:', error);
    }
}

// Fetch and display top products
async function loadTopProducts() {
    try {
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
    } catch (error) {
        console.error('Error loading top products:', error);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    loadSummary();
    loadTopProducts();
});
