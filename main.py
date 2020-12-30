import xml.etree.ElementTree as ET

def printPromoSpotlightRecord(record, keyword): 

    print(keyword, ' : appeard on following rule(s)')
    for pval in record.iterfind('PROP[@name="promo.promoUrl"]/PVAL'):
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

   print("Search for the presence of keywords on the sample promo xml:")
   print(keywords)
   print("***************************************************************")

   for record in records:
     for pval in record.iterfind('PROP[@name="promo.keyword"]/PVAL'):
        if (pval.text.strip().lower() in keywords): 
            printPromoSpotlightRecord(record, pval.text.strip().lower())

def main():
    # parse xml file 
    parseXML('promoData.xml')

if __name__ == "__main__":
    main();