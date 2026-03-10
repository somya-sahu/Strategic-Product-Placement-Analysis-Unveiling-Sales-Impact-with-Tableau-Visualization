import csv
import os

def load_data(file_path):
    rows = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    print(f"Data loaded: {len(rows)} rows")
    return rows

def clean_data(rows):
    seen = set()
    unique_rows = []
    for row in rows:
        key = tuple(sorted(row.items()))
        if key not in seen:
            seen.add(key)
            unique_rows.append(row)
    
    for row in unique_rows:
        sales_before = float(row['Sales_Before'])
        sales_after = float(row['Sales_After'])
        revenue_before = float(row['Revenue_Before'])
        revenue_after = float(row['Revenue_After'])
        conv_before = float(row['Conversion_Rate_Before'])
        conv_after = float(row['Conversion_Rate_After'])
        visibility = float(row['Visibility_Score'])
        traffic = float(row['Traffic_Score'])
        
        row['Sales_Increase'] = round(sales_after - sales_before, 2)
        row['Sales_Growth_Percent'] = round(((sales_after - sales_before) / sales_before * 100), 2)
        row['Revenue_Increase'] = round(revenue_after - revenue_before, 2)
        row['Revenue_Growth_Percent'] = round(((revenue_after - revenue_before) / revenue_before * 100), 2)
        row['Conversion_Improvement'] = round(conv_after - conv_before, 2)
        row['ROI'] = round(((row['Revenue_Increase'] / revenue_before) * 100), 2)
        row['Effectiveness_Score'] = round((visibility * 0.3) + (traffic * 0.3) + (row['Sales_Growth_Percent'] * 0.4), 2)
    
    print(f"Data cleaned: {len(unique_rows)} rows")
    return unique_rows

def save_prepared_data(rows, output_path):
    if not rows:
        return
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    fieldnames = list(rows[0].keys())
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Prepared data saved to: {output_path}")

def generate_summary_stats(rows):
    if not rows:
        return {}
    
    categories = set(r['Category'] for r in rows)
    brands = set(r['Brand'] for r in rows)
    sales_growth = [float(r['Sales_Growth_Percent']) for r in rows]
    revenue_growth = [float(r['Revenue_Growth_Percent']) for r in rows]
    visibility = [float(r['Visibility_Score']) for r in rows]
    revenue_increase = [float(r['Revenue_Increase']) for r in rows]
    
    summary = {
        'Total Products': len(rows),
        'Total Categories': len(categories),
        'Total Brands': len(brands),
        'Avg Sales Growth': f"{sum(sales_growth)/len(sales_growth):.2f}%",
        'Avg Revenue Growth': f"{sum(revenue_growth)/len(revenue_growth):.2f}%",
        'Avg Visibility Score': f"{sum(visibility)/len(visibility):.2f}",
        'Total Revenue Increase': f"${sum(revenue_increase):,.0f}"
    }
    return summary

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_path = os.path.join(script_dir, '../raw_data/product_placement_data.csv')
    prepared_data_path = os.path.join(script_dir, '../data/prepared_data.csv')
    
    rows = load_data(raw_data_path)
    rows_clean = clean_data(rows)
    save_prepared_data(rows_clean, prepared_data_path)
    
    summary = generate_summary_stats(rows_clean)
    print("\n=== Summary Statistics ===")
    for key, value in summary.items():
        print(f"{key}: {value}")
