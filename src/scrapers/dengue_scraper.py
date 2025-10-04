
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime, timedelta

# Selenium setup (GUI ON)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Date range setup
start_date = datetime.strptime("2025-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2025-08-25", "%Y-%m-%d")

# Store data
data = []

previous_total = None

# Loop through each date
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    print(f"Processing date: {date_str}")

    driver.get("https://dashboard.dghs.gov.bd/pages/heoc_dengue_v1")

    # Wait and input date
    wait = WebDriverWait(driver, 20)
    date_input = wait.until(EC.presence_of_element_located((By.NAME, "report_date_filter")))
    date_input.clear()
    date_input.send_keys(date_str)
    date_input.send_keys("\n")

    # Wait for data to load
    time.sleep(10)

    # Parse page
    soup = BeautifulSoup(driver.page_source, "html.parser")
    tables = soup.find_all("table")

    if len(tables) >= 6:
        table_6 = tables[5]
        int_values = []

        for row in table_6.find_all("tr"):
            for cell in row.find_all(["td", "th"]):
                text = cell.get_text(strip=True).replace(",", "")
                if text.isdigit():
                    int_values.append(int(text))

        if int_values:
            total = int_values[-1]
            if previous_total is None:
                dengue_cases = total
            else:
                dengue_cases = total - previous_total
            data.append({
                "Date": date_str,
                "Dengue_Cases": dengue_cases,
                "Total": total
            })
            previous_total = total
        else:
            print(f"No integers found in table 6 for {date_str}")
    else:
        print(f"Less than 6 tables found on {date_str}")

    current_date += timedelta(days=1)

driver.quit()

# Create DataFrame and display
df = pd.DataFrame(data)
df.to_csv("dengue_data.csv", index=False)
print("\n✅ Data saved to dengue_data.csv")
