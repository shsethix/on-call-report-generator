import csv
from datetime import datetime

inputfile = csv.reader(open('finalAlertData 2.csv','r'))
outputfile = open('output_with_extra.csv','w')

i=0

link_placeholder = "https://compass-tech.app.opsgenie.com/alert/detail/%s/details"
team = "Communications and Notifications"
prev = ''

count = 0
duplicates = 0

for row in inputfile:
 
    
    if i==0 :
       place = row[9] + ', ' + row[3] + ', ' + 'link' # +', ' + 'Investigation'
       outputfile.write(place+'\n') 
    else :
        #filter for cando alerts
        if(row[14]==team):
            count+=1

            link = link_placeholder % row[0]
            time = datetime.fromtimestamp(int(int(row[8])/1000))
            place =  str(time) + ', ' + row[3] + ', ' + link 
            #skip if adjacent alerts are same
            if(row[3]!=prev):
                outputfile.write(place+'\n')   
            else:
                duplicates+=1
            prev = row[3]
            
    i+=1

print("Processed %d alerts"%i)
print("duplicates found %d in "%duplicates)
print("Found %d alerts for teams %s" % (count,team))

