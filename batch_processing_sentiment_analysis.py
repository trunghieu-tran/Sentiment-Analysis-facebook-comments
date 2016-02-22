
def read_data_from_CSV_file():
    import csv
    with open('Data/comment_data.csv','r',encoding='utf-8', errors='ignore') as csv_file:
        reader = csv.reader(csv_file, lineterminator='', delimiter=',')
        cnt = 0
        cnt2 = 0
        last = 'Post'
        for row in reader:
            cnt2 += 1
            if row[2] != last:
                cnt += 1
                last = row[2]
                print(last)
        print(cnt)
        print(cnt2)
read_data_from_CSV_file()