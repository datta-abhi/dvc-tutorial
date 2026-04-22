import pandas as pd
from pathlib import Path

# sample data for demonstration
employee_data = {"name": ["Sachin","Sourav", "Dravid"], 
                "salary": [2000, 1800, 1500],
                "department": ["Analytics", "Strategy", "Operations"]}
df = pd.DataFrame(employee_data)

# save data to csv file in employee_data directory
output_dir = Path("employee_data")
output_dir.mkdir(parents=True, exist_ok=True)  # create directory if it doesn't exist
output_file = output_dir / "employee_data.csv"
df.to_csv(output_file, index=False)