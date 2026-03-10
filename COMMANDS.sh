#!/bin/bash
# Strategic Product Placement Analysis - Command Reference
# Copy and paste these commands to execute project phases

# ============================================================================
# PHASE 1: ENVIRONMENT SETUP
# ============================================================================

# Navigate to project directory
cd /home/manish/Code/pythonProject/testing/Strategic-Product-Placement-Analysis-Unveiling-Sales-Impact-with-Tableau-Visualization

# Install Python dependencies
pip install -r requirements.txt

# Verify installation
python -c "import flask, pandas, numpy; print('✅ All dependencies installed')"


# ============================================================================
# PHASE 2: DATA PREPARATION
# ============================================================================

# Run data preparation script
python scripts/data_preparation.py

# Verify prepared data exists
ls -lh data/prepared_data.csv

# Check data shape
python -c "import pandas as pd; df = pd.read_csv('data/prepared_data.csv'); print(f'✅ Data shape: {df.shape}')"

# View first few rows
head -5 data/prepared_data.csv


# ============================================================================
# PHASE 3: START FLASK APPLICATION
# ============================================================================

# Navigate to Flask app directory
cd flask_app

# Run Flask application
python app.py

# In another terminal, test endpoints:
# curl http://localhost:5000
# curl http://localhost:5000/api/summary
# curl http://localhost:5000/api/top-products


# ============================================================================
# PHASE 4: TABLEAU CREATION (Manual Steps)
# ============================================================================

# These steps are done in Tableau Desktop GUI:
# 1. Open Tableau Desktop
# 2. Connect to: data/prepared_data.csv
# 3. Create 8 visualizations (see TABLEAU_SPECIFICATIONS.md)
# 4. Create dashboard with 5 filters
# 5. Create story with 8 scenes
# 6. Publish to Tableau Public
# 7. Get embed codes


# ============================================================================
# PHASE 5: INTEGRATION
# ============================================================================

# After getting Tableau embed codes:
# 1. Edit flask_app/templates/dashboard.html
# 2. Replace placeholder with dashboard embed code
# 3. Edit flask_app/templates/story.html
# 4. Replace placeholder with story embed code
# 5. Save files


# ============================================================================
# PHASE 6: TESTING
# ============================================================================

# Test home page
curl http://localhost:5000

# Test dashboard page
curl http://localhost:5000/dashboard

# Test story page
curl http://localhost:5000/story

# Test API summary
curl http://localhost:5000/api/summary | python -m json.tool

# Test API top products
curl http://localhost:5000/api/top-products | python -m json.tool


# ============================================================================
# PHASE 7: TROUBLESHOOTING
# ============================================================================

# Check if port 5000 is in use
lsof -i :5000

# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Check Python version
python --version

# Check installed packages
pip list | grep -E "Flask|pandas|numpy"

# View Flask app logs
tail -f flask_app/app.py

# Test data file exists
test -f data/prepared_data.csv && echo "✅ Data file exists" || echo "❌ Data file missing"


# ============================================================================
# PHASE 8: DEPLOYMENT (Optional)
# ============================================================================

# Create Procfile for Heroku
echo "web: cd flask_app && python app.py" > Procfile

# Create runtime.txt
echo "python-3.9.0" > runtime.txt

# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: Strategic Product Placement Analysis"

# Deploy to Heroku
heroku create
git push heroku main


# ============================================================================
# USEFUL COMMANDS
# ============================================================================

# View project structure
tree -L 2 -I '__pycache__|*.pyc'

# Count lines of code
find . -name "*.py" -o -name "*.html" -o -name "*.css" -o -name "*.js" | xargs wc -l

# Check file sizes
du -sh *

# View README
cat README.md

# View documentation
cat documentation/PROJECT_DOCUMENTATION.md

# View execution guide
cat EXECUTION_GUIDE.md

# View quick reference
cat QUICK_REFERENCE.md


# ============================================================================
# QUICK START (3 COMMANDS)
# ============================================================================

# 1. Install and prepare
pip install -r requirements.txt && python scripts/data_preparation.py

# 2. Run application
cd flask_app && python app.py

# 3. Access in browser
# Open: http://localhost:5000


# ============================================================================
# MONITORING & DEBUGGING
# ============================================================================

# Monitor Flask app in real-time
watch -n 1 'curl -s http://localhost:5000/api/summary | python -m json.tool'

# Check data statistics
python -c "
import pandas as pd
df = pd.read_csv('data/prepared_data.csv')
print('Data Statistics:')
print(f'Total Records: {len(df)}')
print(f'Total Columns: {len(df.columns)}')
print(f'Avg Sales Growth: {df[\"Sales_Growth_Percent\"].mean():.2f}%')
print(f'Avg Revenue Growth: {df[\"Revenue_Growth_Percent\"].mean():.2f}%')
print(f'Total Revenue Increase: \${df[\"Revenue_Increase\"].sum():,.0f}')
"

# Generate data summary report
python -c "
import pandas as pd
df = pd.read_csv('data/prepared_data.csv')
print('=== DATA SUMMARY REPORT ===')
print(f'Products: {df[\"Product_ID\"].nunique()}')
print(f'Categories: {df[\"Category\"].nunique()}')
print(f'Brands: {df[\"Brand\"].nunique()}')
print(f'Regions: {df[\"Region\"].nunique()}')
print(f'Media Types: {df[\"Media_Type\"].nunique()}')
print(f'Age Groups: {df[\"Consumer_Age_Group\"].nunique()}')
print()
print('Top 5 Products by Sales Growth:')
print(df.nlargest(5, 'Sales_Growth_Percent')[['Product_Name', 'Sales_Growth_Percent']])
"


# ============================================================================
# BACKUP & CLEANUP
# ============================================================================

# Backup project
tar -czf project_backup.tar.gz .

# Clean Python cache
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Remove Flask cache
rm -rf flask_app/__pycache__
rm -rf scripts/__pycache__


# ============================================================================
# DOCUMENTATION COMMANDS
# ============================================================================

# View all documentation
ls -la documentation/
ls -la *.md

# Search documentation
grep -r "Tableau" documentation/
grep -r "API" documentation/
grep -r "filter" documentation/

# Generate documentation index
echo "# Documentation Index" > docs_index.md
echo "" >> docs_index.md
for file in *.md documentation/*.md; do
  echo "- [$file]($file)" >> docs_index.md
done


# ============================================================================
# PERFORMANCE TESTING
# ============================================================================

# Load test API endpoint
for i in {1..10}; do
  curl -s http://localhost:5000/api/summary > /dev/null
  echo "Request $i completed"
done

# Measure response time
time curl http://localhost:5000/api/summary > /dev/null

# Check memory usage
ps aux | grep python


# ============================================================================
# FINAL VERIFICATION
# ============================================================================

# Verify all components
echo "=== PROJECT VERIFICATION ==="
echo ""
echo "✓ Checking files..."
test -f raw_data/product_placement_data.csv && echo "  ✅ Raw data" || echo "  ❌ Raw data missing"
test -f scripts/data_preparation.py && echo "  ✅ Data script" || echo "  ❌ Data script missing"
test -f flask_app/app.py && echo "  ✅ Flask app" || echo "  ❌ Flask app missing"
test -f requirements.txt && echo "  ✅ Requirements" || echo "  ❌ Requirements missing"
echo ""
echo "✓ Checking documentation..."
test -f README.md && echo "  ✅ README" || echo "  ❌ README missing"
test -f EXECUTION_GUIDE.md && echo "  ✅ Execution guide" || echo "  ❌ Execution guide missing"
test -f documentation/PROJECT_DOCUMENTATION.md && echo "  ✅ Full documentation" || echo "  ❌ Full documentation missing"
echo ""
echo "✓ Checking dependencies..."
python -c "import flask; print('  ✅ Flask')" 2>/dev/null || echo "  ❌ Flask not installed"
python -c "import pandas; print('  ✅ Pandas')" 2>/dev/null || echo "  ❌ Pandas not installed"
python -c "import numpy; print('  ✅ NumPy')" 2>/dev/null || echo "  ❌ NumPy not installed"
echo ""
echo "=== VERIFICATION COMPLETE ==="
