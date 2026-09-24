import os
import shutil
from datetime import datetime

# Get current date and time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Calculate Disk Storage stats
total, used, free = shutil.disk_usage("/")
gb = 1024 * 1024 * 1024 # Convert bytes to Gigabytes

report_content = f"""==================================
MAC SYSTEM STATUS REPORT
Generated on: {now}
==================================

💽 HARD DRIVE STORAGE:
----------------------------------
Total Space: {total / gb:.2f} GB
Used Space:  {used / gb:.2f} GB
Free Space:  {free / gb:.2f} GB

🔋 SYSTEM UPTIME LOG:
----------------------------------
"""

print("\nGathering system diagnostics...")

# Create the report file
report_filename = "system_status_log.txt"
with open(report_filename, "w") as report:
    report.write(report_content)

# Append actual live Mac uptime statistics directly into the file
os.system(f"uptime >> {report_filename}")

print(f"🏆 Diagnostics complete! Report saved as: {report_filename}\n")

