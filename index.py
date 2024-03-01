import csv
import json


def parse_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            host = row.get('meta\\.source\\.hostname', '')
            dest = row.get('meta\\.destination\\.hostname', '')
            hop_count = int(row.get('result\\.hop\\.count', 0))
            hop_error_count = int(row.get('result\\.hop\\.error_count', 0))
            ip_list = eval(row.get('result\\.hop\\.ip', '[]'))
            rtt_list = eval(row.get('result\\.json', '[]'))
            
            for i in range(len(ip_list)):
                ip = ip_list[i] if i < len(ip_list) else ''
                hop_data = rtt_list[i] if i < len(rtt_list) else {}
                
                if isinstance(hop_data, list) and hop_data:  
                    rtt_dict = hop_data[0]  
                    rtt = rtt_dict.get("rtt", "N/A")
                    print(rtt_dict)
                    if rtt != "N/A":
                        rtt = rtt.replace("PT", "").replace("S", "")
                    loss = hop_error_count / hop_count if hop_count > 0 else 'N/A'
                elif isinstance(hop_data, dict):
                    rtt = hop_data.get("rtt", "N/A")
                    if rtt != "N/A":
                        rtt = rtt.replace("PT", "").replace("S", "")
                    loss = hop_error_count / hop_count if hop_count > 0 else 'N/A'
                else:
                    rtt, loss = "N/A", "N/A"
                
                data.append([host, dest, hop_count, ip, rtt, loss])

    with open(output_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['host', 'dest', 'hop', 'ip', 'rtt', 'loss'])
        writer.writerows(data)

parse_csv('Sudeste.csv', 'novo_arquivo.csv')



'''
with open('sul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    next(csv_reader)

    meses = {'Jan': '01', 'Feb': '02'}

    for row in csv_reader:
        timer = row[-1].split()
        mes = timer[0]

        for key in meses.keys():
            if mes == key:
                mes = meses[key]
    
        t = f"{timer[2]}-{mes}-{timer[1].replace(',', '')}T"
        
        print(timer)
        print(t)
        raise SystemExit


def parse_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            host = row.get('meta\\.source\\.hostname', '')
            dest = row.get('meta\\.destination\\.hostname', '')
            hop_count = int(row.get('result\\.hop\\.count', 0))
            hop_error_count = int(row.get('result\\.hop\\.error_count', 0))
            ip_list = eval(row.get('result\\.hop\\.ip', '[]'))
            rtt_list = eval(row.get('result\\.json', '[]'))
            
            for i in range(len(ip_list)):
                ip = ip_list[i] if i < len(ip_list) else ''
                hop_data = rtt_list[i] if i < len(rtt_list) else {}
                
                if isinstance(hop_data, list) and hop_data:  
                    rtt_dict = hop_data[0]  
                    rtt = rtt_dict.get('rtt', 'N/A')
                    loss = hop_error_count / hop_count if hop_count > 0 else 'N/A'
                elif isinstance(hop_data, dict):
                    rtt = hop_data.get('rtt', 'N/A')
                    loss = hop_error_count / hop_count if hop_count > 0 else 'N/A'
                else:
                    rtt, loss = 'N/A', 'N/A'
                
                data.append([host, dest, hop_count, ip, rtt, loss])

    with open(output_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['host', 'dest', 'hop', 'ip', 'rtt', 'loss'])
        writer.writerows(data)

parse_csv('sul.csv', 'novo_arquivo.csv')
'''