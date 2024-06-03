import requests
import time

def random_postcode():
    url = "https://www.doogal.co.uk/CreateRandomPostcode/"
    response = requests.get(url)
    data = response.text
    return data.split(",")[0]

def postcode_to_area(postcode):
    print(f"looking for postcode: {postcode}")
    pass_fail = "🔴"
    url = f"https://crystalroof.co.uk/data-api/overview/postcode/v1/{postcode}"
    response = requests.get(url)
    data = response.json()
    income = data["data"]["householdIncomeEnglandWalesMSOA"]["totalAnnualIncomeBucket"]+1
    deprivation = 11-data["data"]["indicesOfDeprivationEnglandLSOA"]["imdDecile"]
    crime = data["data"]["crimeRateLSOA"]["totalBucket"]+1
    if income > 6 and deprivation < 4 and crime < 4:
        pass_fail = "🟢"
    return {
        "pass": pass_fail,
        "income": f"{income}/10",
        "deprivation": f"{deprivation}/10",
        "crime": f"{crime}/10"
    }

def main():
    try:
        postcode = random_postcode()
        # remove whitespace from postcode
        postcode = postcode.replace(" ", "")
        return postcode_to_area(postcode)
    except Exception as e:
        return {"pass": "🔴","error": "Postcode not found"}


while True:
    time.sleep(10)
    print(main())