# Tableau Workbook Specifications

## Dashboard Specifications

### Dashboard Name: "Product Placement Performance Dashboard"

#### Visualizations to Create:

**1. Sales Performance by Category**
- Type: Horizontal Bar Chart
- Dimensions: Category
- Measures: Sales_Growth_Percent (average)
- Filters: Region, Media Type
- Color: Green (positive growth)

**2. Revenue Growth Analysis**
- Type: Line Chart
- Dimensions: Air_Date (continuous)
- Measures: Revenue_Growth_Percent (average)
- Filters: Category, Region
- Trend: Show trend line

**3. Placement Location Effectiveness**
- Type: Heatmap
- Rows: Placement_Location
- Columns: Category
- Color: Effectiveness_Score (average)
- Filters: Region

**4. Consumer Demographics Impact**
- Type: Stacked Bar Chart
- Dimensions: Consumer_Age_Group, Consumer_Gender
- Measures: Sales_Growth_Percent (average)
- Filters: Category, Region

**5. Regional Performance Comparison**
- Type: Map/Geographic
- Dimensions: Region
- Measures: Revenue_Increase (sum)
- Color: Revenue_Growth_Percent (average)
- Size: Total_Revenue_Increase

**6. Media Type Performance**
- Type: Pie Chart
- Dimensions: Media_Type
- Measures: Sales_Growth_Percent (average)
- Filters: Category

**7. Visibility vs Sales Correlation**
- Type: Scatter Plot
- X-axis: Visibility_Score
- Y-axis: Sales_Growth_Percent
- Color: Category
- Size: Revenue_Increase
- Filters: Region

**8. ROI Analysis by Placement Type**
- Type: Horizontal Bar Chart
- Dimensions: Placement_Type
- Measures: ROI (average)
- Color: ROI value (gradient)
- Filters: Category, Region

---

## Dashboard Filters

Add these filters to dashboard:

1. **Category Filter** - Multi-select
2. **Region Filter** - Multi-select
3. **Media Type Filter** - Single/Multi-select
4. **Consumer Age Group Filter** - Multi-select
5. **Date Range Filter** - Air_Date

---

## Story Specifications

### Story Name: "Strategic Product Placement Impact Analysis"

#### Scene 1: Executive Overview
- Title: "Product Placement Performance Overview"
- Visualizations: Summary cards (KPIs)
- Key Metrics:
  - Total Products Analyzed: 30
  - Average Sales Growth: 45.23%
  - Average Revenue Growth: 52.15%
  - Total Revenue Increase: $1,250,000+

#### Scene 2: Category Deep Dive
- Title: "Performance by Product Category"
- Visualization: Sales Performance by Category chart
- Insight: Identify top and bottom performing categories

#### Scene 3: Geographic Insights
- Title: "Regional Performance Analysis"
- Visualization: Regional Performance Comparison map
- Insight: Show regional variations and opportunities

#### Scene 4: Consumer Demographics
- Title: "Demographics Impact on Sales"
- Visualization: Consumer Demographics Impact chart
- Insight: Age group and gender preferences

#### Scene 5: Media Channel Analysis
- Title: "TV vs Movie Placement Effectiveness"
- Visualization: Media Type Performance pie chart
- Insight: Compare media channel effectiveness

#### Scene 6: Placement Strategy
- Title: "Location and Visibility Impact"
- Visualization: Placement Location Effectiveness heatmap
- Insight: Best performing placement locations

#### Scene 7: ROI & Effectiveness
- Title: "Financial Performance Metrics"
- Visualization: ROI Analysis by Placement Type
- Insight: Return on investment analysis

#### Scene 8: Strategic Recommendations
- Title: "Actionable Insights & Recommendations"
- Key Recommendations:
  1. Prioritize high-traffic locations
  2. Use close-up placements for premium products
  3. Target 25-34 demographic
  4. Leverage TV placements
  5. Optimize placement duration

---

## Calculated Fields in Tableau

Create these calculated fields in Tableau:

1. **Sales_Increase**
   ```
   [Sales_After] - [Sales_Before]
   ```

2. **Sales_Growth_Percent**
   ```
   ([Sales_After] - [Sales_Before]) / [Sales_Before] * 100
   ```

3. **Revenue_Increase**
   ```
   [Revenue_After] - [Revenue_Before]
   ```

4. **Revenue_Growth_Percent**
   ```
   ([Revenue_After] - [Revenue_Before]) / [Revenue_Before] * 100
   ```

5. **Conversion_Improvement**
   ```
   [Conversion_Rate_After] - [Conversion_Rate_Before]
   ```

6. **ROI**
   ```
   ([Revenue_Increase] / [Revenue_Before]) * 100
   ```

7. **Effectiveness_Score**
   ```
   ([Visibility_Score] * 0.3) + ([Traffic_Score] * 0.3) + ([Sales_Growth_Percent] * 0.4)
   ```

---

## Dashboard Design Guidelines

- **Color Scheme**: 
  - Primary: #2c3e50 (Dark Blue)
  - Accent: #3498db (Light Blue)
  - Success: #27ae60 (Green)
  - Warning: #e74c3c (Red)

- **Layout**: 
  - 2-3 columns for desktop
  - Single column for mobile
  - Responsive design

- **Interactivity**:
  - All charts linked to filters
  - Drill-down capabilities
  - Hover tooltips with details

---

## Publishing to Tableau Public

1. Save workbook as `.twbx`
2. Sign in to Tableau Public
3. Publish workbook
4. Set permissions (Public/Private)
5. Get embed code from Share button
6. Copy embed code to Flask templates

---

## Performance Optimization

- Limit data to last 12 months
- Use aggregated data for large datasets
- Optimize filter performance
- Cache frequently accessed views
- Monitor query performance

---

## Testing Checklist

- [ ] All filters work correctly
- [ ] Visualizations update on filter change
- [ ] Drill-down functionality works
- [ ] Tooltips display correct information
- [ ] Dashboard loads within 5 seconds
- [ ] Mobile responsive design works
- [ ] Story scenes transition smoothly
- [ ] Embed codes work in Flask app
