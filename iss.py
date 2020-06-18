import requests

def main():

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

    def answer():
        if list(r2check.keys())[0] == 'codes':
            Country = r2.json()["countryName"]
            Area =  r2.json()["adminName1"]
            if Country in Area:
                print(Area)
                return Area
            else:
                print(Area + ", " + Country)
                return Area + ", " + Country
        else:
            print(r3.json()["ocean"]["name"])
            return r3.json()["ocean"]["name"]

    answer()

if __name__ == "__main__":
    main()