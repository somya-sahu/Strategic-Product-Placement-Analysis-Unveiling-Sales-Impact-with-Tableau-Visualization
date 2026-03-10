import csv
import json
import os
from datetime import datetime

class DataCollection:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = []
        self.metadata = {}
        self.load_data()
    
    def load_data(self):
        """Load data from CSV file"""
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r') as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
            self.metadata['total_records'] = len(self.data)
            self.metadata['fields'] = list(self.data[0].keys()) if self.data else []
            self.metadata['load_time'] = datetime.now().isoformat()
        return self.data
    
    def get_data_summary(self):
        """Get comprehensive data summary"""
        if not self.data:
            return {}
        
        summary = {
            'total_records': len(self.data),
            'total_fields': len(self.metadata['fields']),
            'fields': self.metadata['fields'],
            'data_quality': self.assess_data_quality(),
            'statistics': self.calculate_statistics()
        }
        return summary
    
    def assess_data_quality(self):
        """Assess data quality metrics"""
        if not self.data:
            return {}
        
        total_cells = len(self.data) * len(self.metadata['fields'])
        empty_cells = 0
        
        for row in self.data:
            for value in row.values():
                if not value or value.strip() == '':
                    empty_cells += 1
        
        completeness = round((1 - empty_cells / total_cells) * 100, 2) if total_cells > 0 else 0
        
        return {
            'completeness_percent': completeness,
            'total_cells': total_cells,
            'empty_cells': empty_cells,
            'data_quality_score': completeness
        }
    
    def calculate_statistics(self):
        """Calculate statistical measures"""
        if not self.data:
            return {}
        
        stats = {}
        
        # Numeric fields analysis
        numeric_fields = ['Sales_Before', 'Sales_After', 'Revenue_Before', 'Revenue_After',
                         'Visibility_Score', 'Traffic_Score', 'Sales_Growth_Percent', 
                         'Revenue_Growth_Percent', 'Conversion_Rate_Before', 'Conversion_Rate_After']
        
        for field in numeric_fields:
            values = []
            for row in self.data:
                try:
                    val = float(row.get(field, 0))
                    values.append(val)
                except:
                    pass
            
            if values:
                stats[field] = {
                    'min': round(min(values), 2),
                    'max': round(max(values), 2),
                    'avg': round(sum(values) / len(values), 2),
                    'count': len(values)
                }
        
        return stats
    
    def get_categorical_analysis(self):
        """Analyze categorical variables"""
        if not self.data:
            return {}
        
        categorical_fields = ['Category', 'Region', 'Media_Type', 'Consumer_Age_Group', 
                             'Consumer_Gender', 'Placement_Location', 'Placement_Type']
        
        analysis = {}
        
        for field in categorical_fields:
            categories = {}
            for row in self.data:
                value = row.get(field, 'Unknown')
                categories[value] = categories.get(value, 0) + 1
            
            analysis[field] = {
                'unique_values': len(categories),
                'distribution': categories,
                'most_common': max(categories, key=categories.get) if categories else None,
                'least_common': min(categories, key=categories.get) if categories else None
            }
        
        return analysis
    
    def filter_data(self, field, value):
        """Filter data by field and value"""
        filtered = [row for row in self.data if row.get(field) == value]
        return filtered
    
    def get_top_performers(self, metric='Sales_Growth_Percent', limit=10):
        """Get top performing products by metric"""
        try:
            sorted_data = sorted(self.data, 
                               key=lambda x: float(x.get(metric, 0)), 
                               reverse=True)
            return sorted_data[:limit]
        except:
            return []
    
    def get_bottom_performers(self, metric='Sales_Growth_Percent', limit=10):
        """Get bottom performing products by metric"""
        try:
            sorted_data = sorted(self.data, 
                               key=lambda x: float(x.get(metric, 0)))
            return sorted_data[:limit]
        except:
            return []
    
    def generate_insights(self):
        """Generate key insights from data"""
        if not self.data:
            return {}
        
        insights = {}
        
        # Sales growth insights
        sales_growth = [float(r.get('Sales_Growth_Percent', 0)) for r in self.data]
        insights['avg_sales_growth'] = round(sum(sales_growth) / len(sales_growth), 2)
        insights['max_sales_growth'] = round(max(sales_growth), 2)
        insights['min_sales_growth'] = round(min(sales_growth), 2)
        
        # Revenue insights
        revenue_increase = [float(r.get('Revenue_Increase', 0)) for r in self.data]
        insights['total_revenue_increase'] = round(sum(revenue_increase), 2)
        insights['avg_revenue_increase'] = round(sum(revenue_increase) / len(revenue_increase), 2)
        
        # Category performance
        categories = {}
        for row in self.data:
            cat = row.get('Category', 'Unknown')
            growth = float(row.get('Sales_Growth_Percent', 0))
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(growth)
        
        insights['category_performance'] = {
            cat: round(sum(vals) / len(vals), 2) 
            for cat, vals in categories.items()
        }
        
        # Regional performance
        regions = {}
        for row in self.data:
            reg = row.get('Region', 'Unknown')
            growth = float(row.get('Sales_Growth_Percent', 0))
            if reg not in regions:
                regions[reg] = []
            regions[reg].append(growth)
        
        insights['regional_performance'] = {
            reg: round(sum(vals) / len(vals), 2) 
            for reg, vals in regions.items()
        }
        
        return insights
    
    def export_report(self, filename):
        """Export comprehensive data report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'data_summary': self.get_data_summary(),
            'categorical_analysis': self.get_categorical_analysis(),
            'insights': self.generate_insights(),
            'top_performers': self.get_top_performers(),
            'bottom_performers': self.get_bottom_performers()
        }
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        return report

# Usage example
if __name__ == '__main__':
    data_path = 'data/prepared_data.csv'
    
    # Initialize data collection
    collector = DataCollection(data_path)
    
    # Get data summary
    print("=== DATA COLLECTION SUMMARY ===")
    summary = collector.get_data_summary()
    print(f"Total Records: {summary['total_records']}")
    print(f"Total Fields: {summary['total_fields']}")
    print(f"Data Quality Score: {summary['data_quality']['data_quality_score']}%")
    
    # Get categorical analysis
    print("\n=== CATEGORICAL ANALYSIS ===")
    categorical = collector.get_categorical_analysis()
    for field, analysis in categorical.items():
        print(f"\n{field}:")
        print(f"  Unique Values: {analysis['unique_values']}")
        print(f"  Most Common: {analysis['most_common']}")
    
    # Get insights
    print("\n=== KEY INSIGHTS ===")
    insights = collector.generate_insights()
    print(f"Average Sales Growth: {insights['avg_sales_growth']}%")
    print(f"Total Revenue Increase: ${insights['total_revenue_increase']:,.0f}")
    
    # Export report
    collector.export_report('data_collection_report.json')
    print("\nReport exported to: data_collection_report.json")
