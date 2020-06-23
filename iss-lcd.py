import requests
import Adafruit_CharLCD as LCD
import time

def main():
    def program():
        while True:
            #This part is the pin mapping on PI to LCD
            lcd_rs        = 25
            lcd_en        = 24
            lcd_d4        = 23
            lcd_d5        = 17
            lcd_d6        = 18
            lcd_d7        = 22
            lcd_backlight = 2

            #Define LCD column and row size for 16x2 LCD.
            lcd_columns = 16
            lcd_rows = 2

            lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

            #Get them lat and longs of the IIS!
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

            #Make a variable with  the request as a dictionary value
            r2check = r2.json()
            r3check = r3.json()

            def answer():
            #if dictionary contains "codes" key then country returned:
                if "codes" in r2check:
                    Country = r2.json()["countryName"]
                    Area = r2.json()["adminName1"]
                    #This is to avoid repeating country names in regions
                    if Country in Area:
                        return Area
                    else:
                        return Area + ", " + Country
                else:
                   # return r3.json()["ocean"]["name"]
                   # return r3.json()["name"]
                    if "ocean" in r3check:
                        Ocean = r3check["ocean"]["name"]
                        return Ocean
                    else:
                        return "No Data"

            #Output to LCD
            lcd.message("ISS location:\n" + answer())

            #Print to terminal
            print(answer())

            answer()
            print(r2.content + r3.content)
            time.sleep(15.0)

    program()

if __name__ == "__main__":
    main()
