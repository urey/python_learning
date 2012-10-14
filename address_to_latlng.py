#-------------------------------------------------------------------------------
# Name:        google maps address to latitute & longitute
# Purpose:
#
# Author:      urey
#
# Created:     14/10/2012
# Copyright:   (c) urey 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from googlemaps import GoogleMaps

def main():
    address = 'beihang university'
    print GoogleMaps().address_to_latlng(address)
    pass

if __name__ == '__main__':
    main()
