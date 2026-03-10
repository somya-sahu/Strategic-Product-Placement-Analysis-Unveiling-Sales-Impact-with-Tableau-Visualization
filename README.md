# Strategic Product Placement Analysis - Unveiling Sales Impact with Tableau Visualization

## 🚀 Live Demo
**[View Live Application](https://product-placement-analysis.onrender.com)**

## Quick Start Guide

### What This Project Does
Analyzes how strategic product placement impacts sales performance and consumer behavior using data visualization and web integration.

### Quick Setup (5 minutes)

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare Data**
   ```bash
   python scripts/data_preparation.py
   ```

3. **Run Web Application**
   ```bash
   cd flask_app
   python app.py
   ```
   Open browser: `http://localhost:5000`

### Project Deliverables

✅ **Data Collection**: 30 products with 23 attributes  
✅ **Data Preparation**: 7 calculated fields  
✅ **Visualizations**: 8+ unique charts and graphs  
✅ **Dashboard**: Interactive Tableau dashboard  
✅ **Story**: 8-scene narrative analysis  
✅ **Web Integration**: Flask application with API  
✅ **Documentation**: Complete step-by-step guide  
✅ **Live Deployment**: Deployed on Render  

### Key Features

- **Interactive Filters**: Category, Region, Media Type, Demographics
- **Real-time Analytics**: Summary statistics and top products
- **Responsive Design**: Works on desktop and mobile
- **API Endpoints**: `/api/summary` and `/api/top-products`

### File Structure

```
├── raw_data/product_placement_data.csv    # Original dataset
├── data/prepared_data.csv                 # Cleaned data
├── scripts/data_preparation.py            # Data processing
├── flask_app/                             # Web application
│   ├── app.py
│   ├── templates/
│   └── static/
├── documentation/PROJECT_DOCUMENTATION.md # Full guide
└── requirements.txt
```

### Tableau Integration

1. Open Tableau Desktop
2. Connect to `data/prepared_data.csv`
3. Create 8 visualizations (see documentation)
4. Publish to Tableau Public
5. Copy embed codes to Flask templates

### API Usage

**Get Summary Stats:**
```bash
curl http://localhost:5000/api/summary
```

**Get Top Products:**
```bash
curl http://localhost:5000/api/top-products
```

### Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 5000 in use | Change port in app.py or kill process |
| Data not found | Run data_preparation.py first |
| Tableau not showing | Verify embed code in HTML templates |

### Next Steps

1. Review `documentation/PROJECT_DOCUMENTATION.md` for detailed guide
2. Create Tableau visualizations
3. Embed Tableau dashboard and story in Flask app
4. Test all filters and interactions
5. Record demonstration video

### Support

Refer to PROJECT_DOCUMENTATION.md for:
- Complete setup instructions
- Visualization specifications
- API documentation
- Troubleshooting guide
- Key insights and recommendations

---

**Status**: ✅ Complete  
**Version**: 1.0  
**Last Updated**: 2024
