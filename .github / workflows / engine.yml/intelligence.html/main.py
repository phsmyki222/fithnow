import urllib.request
import datetime

def check_phrinusomyis():
    url = "https://phrinusomyis.com"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Checking the connection to your authority domain
        response = urllib.request.urlopen(url)
        status = response.getcode()
        
        if status == 200:
            print(f"[{current_time}] PHRINUSOMYIS is Online. SEO Status: Active.")
        else:
            print(f"[{current_time}] Alert: Site responded with status {status}")
            
    except Exception as e:
        print(f"[{current_time}] Critical: Could not reach domain. Error: {e}")

if __name__ == "__main__":
    print("PHRINUSOMYIS 24/7 Engine Starting...")
    check_phrinusomyis()

