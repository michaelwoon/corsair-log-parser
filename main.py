import csv
import re
from datetime import datetime

logs = []
ips = {}
days = [1, 5, 19, 23, 24, 25]
with open('logs.csv', newline='') as csvfile:
    logreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in logreader:
        if row[0] ==  'timestamp':
            continue
        timeint = int(row[0])
        date = datetime.fromtimestamp(timeint/1000.0)
        if date.month == 8 and date.day in days:
            logs.append([str(date), row[1], row[2]])

            ipregex = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
            results = ipregex.search(row[2])
            if results != None:
                if results[0] in ips:
                    ips[results[0]] += 1
                else:
                    ips[results[0]] = 1

parsedLogs = []
with open('logs.csv', newline='') as csvfile:
    logreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in logreader:
        if row[0] ==  'timestamp':
            continue
        if "129.205.113.181" in row[2]:
            timeint = int(row[0])
            date = datetime.fromtimestamp(timeint/1000.0)

            filename = 'parsed/' + str(date.month) + '_' + str(date.day) + '.csv'
            with open(filename, 'a') as writefile:
                logwriter = csv.writer(writefile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                logwriter.writerow([str(date), row[1], row[2]])



# print(ips) 179.7.192.170
# second one 129.205.113.181
sortedIps = sorted(ips.items(), key=lambda x: x[1])
# for i in sortedIps:
# 	print(i[0], i[1])
print(len(logs))
print(logs[0])
