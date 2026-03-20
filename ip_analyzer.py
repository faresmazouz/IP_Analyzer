import requests


def get_ip_info(ip_address):

    url = f"https://ipinfo.io/{ip_address}/json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "bogon" in response.json():
            print("The IP address is private or invalid (non-routable).")
            return None

        return data

    except requests.RequestException as e:
        print(f"Error fetching IP information: {e}")
        return None


def analyze_ip(ip_address):

    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    org = data.get("org", "N/A")
    country = data.get("country", "N/A")
    

    analysis =[]

    if "Google" in org:
        analysis.append("This IP address is associated with Google.")
    elif "Amazon" in org:
        analysis.append("This IP address is associated with Amazon.")
    elif "Microsoft" in org:
        analysis.append("This IP address is associated with Microsoft.")
    elif "Cloudflare" in org:
        analysis.append("This IP address is associated with Cloudflare.")
    else:
        analysis.append("This IP address is not associated with major tech companies.")

    if country == "US":
        analysis.append("This IP address is located in the United States.")
    elif country == "CN":
        analysis.append("This IP address is located in China.")
    elif country == "RU":
        analysis.append("This IP address is located in Russia.")
    else:
        analysis.append(f"This IP address is located in {country}.")    

    return " ".join(analysis)

def display_ip_info(data):
    print(f"IP Address: {data.get('ip', 'N/A')}")
    print(f"Hostname: {data.get('hostname', 'N/A')}")
    print(f"City: {data.get('city', 'N/A')}")
    print(f"Region: {data.get('region', 'N/A')}")
    print(f"Country: {data.get('country', 'N/A')}")
    print(f"Location: {data.get('loc', 'N/A')}")
    print(f"Organization: {data.get('org', 'N/A')}")

def main():
    print("====IP Address Analyzer====")
    ip_address = input("Enter an IP address to analyze: ").strip()

    if not ip_address:
        print("No IP address entered. Exiting.")
        return

    data = get_ip_info(ip_address)

    if data:
        display_ip_info(data)
        analysis = analyze_ip(ip_address)
        print("\n====Analysis====")
        print(analysis)

if __name__ == "__main__":
    main()
