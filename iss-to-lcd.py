import requests
import time

def main():
    def program():
        while True:
            r1 = requests.get("http://api.open-notify.org/iss-now.json")

            #Make the responce json into a python dict#
            isspos = r1.json()["iss_position"]

            #Build the geonames URL#
            geouser = 'jheath11011'
            geonames_url = 'http://api.geonames.org/'
            urlcountry = geonames_url + 'countrySubdivisionJSON?lat=' + isspos["latitude"] + '&lng=' + isspos["longitude"] + '&username=' + geouser
            urlocean = geonames_url + 'oceanJSON?lat=' + isspos["latitude"] + '&lng=' + isspos["longitude"] + '&username=' + geouser

            #Call the geonames api#
            r2 = requests.get(urlcountry)
            r3 = requests.get(urlocean)

            r2check = r2.json()
            r3check = r3.json()

            def answer():
                if "codes" in r2check:
                    Country = r2.json()["countryName"]
                    Area =  r2.json()["adminName1"]
                    if Country in Area:
                        print(Area)
                        return Area
                    else:
                        print(Area + ", " + Country)
                        return Area + ", " + Country
                else:
                    Ocean = r3check["ocean"]["name"]
                    print(Ocean)
                    return Ocean

            answer()
            time.sleep(15.0)
    program()
if __name__ == "__main__":
    main()