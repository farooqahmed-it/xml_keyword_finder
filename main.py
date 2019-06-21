
import requests 
import xml.etree.ElementTree as ET

def loadPromotionsData(): 
  
    # url of Promotions feed 
    url = 'https://www.fishersci.com/libs/services/wcm/Exporter?type=content-spotlights&locale=en_US'
  
    # creating HTTP response object from given url 
    resp = requests.get(url) 
  
    # saving the xml file 
    with open('contentSpotlightData.xml', 'wb') as f: 
        f.write(resp.content)
        f.close() 

def printContentSpotlightRecord(record, keyword): 

    print(keyword, ' : appeard on following page')
    for pval in record.iterfind('PROP[@name="workbench.pageUrl"]/PVAL'):
        print('\t', pval.text )

def parseXML(xmlfile): 
   keywords=[]

   # use the parse() function to load and parse an XML file
   tree = ET.parse(xmlfile)
   records = tree.getroot()

   file = open('keywords.txt', 'r')
   for line in file.readlines():
     keywords.append((line.strip().lower()))

   file.close()  

   print("Search for the presence of keywords on the existing content spotlight:")
   print(keywords)
   print("*********************************************************************************************************************************************")

   for record in records:
     for pval in record.iterfind('PROP[@name="workbench.keyword"]/PVAL'):
        if (pval.text.strip().lower() in keywords): 
            printContentSpotlightRecord(record, pval.text.strip().lower())

def main():
    #Load promotions Data
    loadPromotionsData()

    # parse xml file 
    parseXML('promoData.xml')

if __name__ == "__main__":
    main();