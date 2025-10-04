from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import date, timedelta
import time

def fetch_daily_data(station='bd/dhaka/VGHS', target_date='2025-01-01'):
    url = f"https://www.wunderground.com/history/daily/{station}/date/{target_date}"

    # Chrome browser visible (headed mode)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    print(f"Opening: {url}")
    driver.get(url)

    try:
        table = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        df = pd.read_html(table.get_attribute('outerHTML'))[0]
    except Exception as e:
        print(f"❌ Error on {target_date}: {e}")
        df = pd.DataFrame()
    
    driver.quit()
    return df


# 🔁 Main loop: 1 Jan to 25 Aug 2025
start_date = date(2025, 1, 1)
end_date = date(2025, 8, 25)

all_data = []

current = start_date
while current <= end_date:
    print(f"\n📅 Scraping: {current.isoformat()}")
    try:
        daily_df = fetch_daily_data(target_date=current.isoformat())
        if not daily_df.empty:
            # Drop NaNs
            daily_df.dropna(subset=["Time", "Temperature", "Humidity"], inplace=True)

            # Add Date
            daily_df['Date'] = current.isoformat()

            # Convert Temperature to Celsius
            daily_df['Temperature (°C)'] = (
                daily_df['Temperature']
                .str.extract(r'(\d+)')
                .astype(float)
                .apply(lambda x: round((x - 32) * 5 / 9))
            )

            # Clean Humidity: remove extra characters, keep only numbers
            daily_df['Humidity'] = (
                daily_df['Humidity']
                .astype(str)
                .str.extract(r'(\d+)')
                .astype(float)
            )

            # Filter only needed columns and rename Humidity column
            filtered = daily_df[['Date', 'Time', 'Temperature (°C)', 'Humidity']].copy()
            filtered.rename(columns={'Humidity': 'Humidity (in %)'}, inplace=True)


            all_data.append(filtered)
        else:
            print("⚠️ No data found.")
    except Exception as e:
        print(f"❌ Failed on {current}: {e}")
    
    current += timedelta(days=1)
    time.sleep(1.5)  # delay to avoid being blocked

# Combine all data
if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    final_df.to_csv("weather_dhaka_2025.csv", index=False)
    print("\n✅ Scraping complete. Data saved to 'weather_dhaka_2025.csv'")
else:
    print("😕 No data was scraped.")
