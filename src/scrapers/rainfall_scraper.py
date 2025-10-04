from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time
import pandas as pd

def scrape_rainfall_with_selenium(date_str):
    url = f"https://live8.bmd.gov.bd/map/1/d/{date_str}"
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Headless mode for speed
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        # Wait until the rainfall element is present
        forecast_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#map_left .forcastvalue .forecastbox .small .left")
            )
        )

        rainfall_text = forecast_element.text.strip()

        # Example text: "Rainfall : 0.0 mm"
        # Extract just the numeric part
        if "Rainfall" in rainfall_text:
            numeric_str = rainfall_text.split(":")[1].strip().split()[0]  # "0.0"
            rainfall_value = float(numeric_str)
        else:
            rainfall_value = None  # Or 0.0 if you prefer

        return {
            "Date": date_str,
            "Rainfall_mm": rainfall_value
        }

    except Exception as e:
        print(f"Error on {date_str}: {e}")
        return {
            "Date": date_str,
            "Rainfall_mm": None
        }

    finally:
        driver.quit()


if __name__ == "__main__":
    start_date = datetime.strptime("2025-01-01", "%Y-%m-%d")
    end_date = datetime.strptime("2025-08-25", "%Y-%m-%d")

    delta = timedelta(days=1)
    current_date = start_date

    all_data = []

    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        print(f"Scraping data for {date_str}...")
        data = scrape_rainfall_with_selenium(date_str)
        all_data.append(data)
        current_date += delta
        time.sleep(1)  # Optional: slow down requests

    df = pd.DataFrame(all_data)
    df.to_csv("rainfall_data_2025.csv", index=False)
