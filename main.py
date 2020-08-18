import csv
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()


def read_json(url):
    response = http.request('GET', url)
    read = json.loads(response.data)

    split_paid = read['paid']
    for i in split_paid:
        print("Name:", i['confName'] + "," + " Date:", i['confStartDate'] + "," + " Venue:",
              i['venue'] + " , " + " City:", i['city'] + " , " + " Type:", i['entryType'] + " , " + " Link:",
              i['confUrl'])
        print()

    split_free = read['free']
    for i in split_free:
        print("Name:", i['confName'] + "," + " Date:", i['confStartDate'] + "," + " Venue:",
              i['venue'] + " , " + " City:", i['city'] + " , " + " Type:", i['entryType'] + " , " + " Link:",
              i['confUrl'])
        print()
    return split_paid + split_free


def required(conf):
    for i in conf:
        val = [i['confName'], i['confStartDate'], i['venue'], i['state'], i['country'], i['entryType'], i['confRegUrl'], i['searchTerms']]
        for x in val:
            if x != "":
                values = val
        needed_data = ", ".join(values)
        return needed_data


def diff(a, b):
    count = 0
    for key in a.keys():
        if a[key] != b[key]:
            count = count + 1
    return count


def remove_duplicates(conf):
    dup = []
    for i in range(0,len(conf)):
        for j in range(0, i):
            diffi = diff(conf[i], conf[j])
            if diffi <= 5:
                dup.append(conf[i])
    return dup


def generate_csv(conf):
    with open('data.csv', 'w') as f:
        w = csv.writer(f)
        w.writerow(conf[0].keys())
        for conf in conf:
            w.writerow(conf.values())
    print("csv file created")


if __name__ == "__main__":
    link = "https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences"
    conf = read_json(link)
    required(conf)
    remove_duplicates(conf)
    dup = remove_duplicates(conf)
    print(required(dup))
    generate_csv(conf)





