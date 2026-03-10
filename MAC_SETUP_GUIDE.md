# Mac Environment - Visualization Setup Guide

## ✅ Fixed for Mac Environment

### Issue Resolved
- Chart.js CDN updated to CDN.js (more reliable on Mac)
- Canvas rendering optimized for macOS
- Responsive height containers added
- System fonts configured for Mac

---

## 🚀 Quick Start on Mac

### Step 1: Navigate to Project
```bash
cd /home/manish/Code/pythonProject/testing/Strategic-Product-Placement-Analysis-Unveiling-Sales-Impact-with-Tableau-Visualization
```

### Step 2: Prepare Data
```bash
python3 scripts/data_preparation.py
```

### Step 3: Start Server
```bash
python3 flask_app/server.py
```

### Step 4: Open in Browser
```
http://localhost:5000/visualizations
```

---

## 🔧 Mac-Specific Fixes Applied

### 1. Chart.js CDN
- Changed from: `cdn.jsdelivr.net`
- Changed to: `cdnjs.cloudflare.com`
- More reliable on macOS

### 2. Canvas Rendering
- Added `maintainAspectRatio: false`
- Added explicit height containers
- Fixed responsive sizing

### 3. System Fonts
- Added `-apple-system` font stack
- Added `BlinkMacSystemFont`
- Better rendering on macOS

### 4. Chart Options
- Simplified chart configuration
- Removed complex nested options
- Optimized for Safari/Chrome on Mac

---

## 📊 Visualizations Now Working

### Pie Charts (2)
- Sales Growth by Category
- Revenue by Region

### Bar Charts (2)
- Sales Performance
- Revenue Growth

### Line Charts (2)
- Sales Trend
- Revenue Trend

### Scatter Plots (1)
- Visibility vs Sales

### Doughnut Charts (1)
- Brand Distribution

### Radar Charts (1)
- Performance Metrics

**Total: 9 Interactive Charts**

---

## ✅ Verification Steps

### 1. Check Server Running
```bash
curl http://localhost:5000/
```
Should return HTML

### 2. Check Visualizations Page
```bash
curl http://localhost:5000/visualizations | grep "categoryPie"
```
Should return matches

### 3. Check API
```bash
curl http://localhost:5000/api/summary
```
Should return JSON

---

## 🐛 Troubleshooting

### Charts Not Showing
**Solution**: Clear browser cache
```bash
# Safari: Cmd+Shift+Delete
# Chrome: Cmd+Shift+Delete
# Firefox: Cmd+Shift+Delete
```

### Port Already in Use
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Or use different port
python3 flask_app/server.py --port 5001
```

### Chart.js Not Loading
**Solution**: Check internet connection (CDN requires it)

### Slow Performance
**Solution**: Reduce number of data points or use Safari

---

## 📱 Browser Compatibility

### Recommended Browsers
- ✅ Safari (Best on Mac)
- ✅ Chrome
- ✅ Firefox
- ✅ Edge

### Minimum Requirements
- macOS 10.12+
- Modern browser
- JavaScript enabled
- Internet connection (for CDN)

---

## 🎯 Features Working

- ✅ All 9 charts rendering
- ✅ Responsive design
- ✅ Interactive tooltips
- ✅ Legend toggles
- ✅ Smooth animations
- ✅ Mobile friendly

---

## 📊 Data Displayed

### Key Metrics
- Total Products: 30
- Avg Sales Growth: 43.37%
- Avg Revenue Growth: 43.37%
- Total Revenue Increase: $1,031,500

### Categories
- Electronics, Accessories, Beverages
- Food, Apparel, Beauty, Footwear

### Regions
- North America, Europe, Asia

---

## 🔗 Access Points

```
Home: http://localhost:5000/
Visualizations: http://localhost:5000/visualizations
Dashboard: http://localhost:5000/dashboard
Story: http://localhost:5000/story
API Summary: http://localhost:5000/api/summary
API Top Products: http://localhost:5000/api/top-products
```

---

## ✨ Mac Optimization Tips

1. **Use Safari**: Best performance on macOS
2. **Close Other Apps**: Free up memory
3. **Clear Cache**: Cmd+Shift+Delete
4. **Disable Extensions**: May interfere with charts
5. **Check Internet**: CDN requires connection

---

## 🎉 Status

**Mac Environment**: ✅ FIXED  
**Visualizations**: ✅ WORKING  
**Charts**: ✅ 9 RENDERING  
**Ready to Use**: ✅ YES

---

**Version**: 1.0  
**Last Updated**: 2024  
**Platform**: macOS  
**Status**: WORKING ✅
