import csv

inputfile = csv.reader(open('input.csv','r'))
outputfile = open('output.csv','w')

i=0

link_placeholder = "https://compass-tech.app.opsgenie.com/alert/detail/%s/details"

for row in inputfile:
 
    if i==0 :
       place = row[9] + ', ' + row[3] + ', ' + 'link'
    else :
        link = link_placeholder % row[0]
        place = row[9] + ', ' + row[3] + ', ' + link

    print(place)
    outputfile.write(place+'\n')       
    i+=1