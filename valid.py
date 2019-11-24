'''
Adapun kriteria nomor kartu kredit yang valid adalah sebagai berikut:

Diawali dengan angka 4, 5 atau 6.
Terdiri atas tepat 16 digit angka.
Hanya mengandung angka 0-9.
Boleh dituliskan berupa grup 4 digit yang dipisahkan dengan tanda hubung "-"
Tidak boleh terdapat 1 angka yang diulang >3x & tertulis secara beruntun, misal: 3333.
Contoh:

✅ Nomor kartu kredit valid:

4253625879615781
4424424424442442
5122-2368-7954-3213
4123456789123454
5123-4567-8912-3455
4123356789123456
❌ Nomor kartu kredit invalid:

0525362587961578    (tidak diawali dengan 4, 5 atau 6)
42536258796157867    (terdiri atas 17 digit angka)
44244z4424442444    (terdapat karakter 'z' yang bukan angka)
5122.2368.7954.3214    (dipisahkan bukan dengan tanda hubung)
4424444424442444    (terdapat angka yang diulang >3x & tertulis secara beruntun, yaitu: 44444)
61234-123-8912-3456    (terdapat grup yang tidak hanya terdiri atas 4 digit angka)
5199-9967-7912-3457    (terdapat angka yang diulang >3x & tertulis secara beruntun, yaitu: 9999)
5123 - 4567 - 8912 - 3456    (dipisahkan dengan tanda hubung & spasi)
Output yang diharapkan:

File ccValid.json berisi data nasabah dengan nomor kartu kredit yang valid:
[
    {"nama": "Andi", "noCreditCard": "4253625879615781"},
    {"nama": "Budi", "noCreditCard": "5123-4567-8912-3455"},
    {"nama": "Euis", "noCreditCard": "4424424424442442"},
    {"nama": "Inne", "noCreditCard": "5122-2368-7954-3213"},
    {"nama": "Nuri", "noCreditCard": "4123356789123456"},
    {"nama": "Opik", "noCreditCard": "4123456789123454"}
]
File ccInvalid.json berisi data nasabah dengan nomor kartu kredit yang tidak valid:
[
    {"nama": "Caca", "noCreditCard": "0525362587961578"},
    {"nama": "Deni", "noCreditCard": "42536258796157867"},
    {"nama": "Fani", "noCreditCard": "44244z4424442444"},
    {"nama": "Gaga", "noCreditCard": "5122.2368.7954.3214"},
    {"nama": "Hari", "noCreditCard": "4424444424442444"},
    {"nama": "Janu", "noCreditCard": "61234-123-8912-3456"},
    {"nama": "Kiki", "noCreditCard": "5199-9967-7912-3457"},
    {"nama": "Luis", "noCreditCard": "1111222233334444"},
    {"nama": "Mira", "noCreditCard": "5123 - 4567 - 8912 - 3456"}
]
'''

# Jawaban

import json

def cekDepan(param):
    # print(param[0])
    if int(param[0]) == 4 or int(param[0]) == 5 or int(param[0]) == 6:
        return True
    else:
        return False

def cekTitik(param):
    titik = '.'
    if titik in str(param):
        return False
    else:
        return True

def cekPanjang(param):
    if len(str(param).replace('-', '')) == 16:
        return True
    else:
        return False

def cekAngka(param):
    if str(param).replace('-', '').isnumeric():
        return True
    else:
        return False

def cekUlang(param):
    newList = list(str(param).replace('-', ''))
    print(newList)
    count = 0

    for i in range(len(newList)-1):
        print(count, end= "")
        if newList[i] == newList[i+1]:
            count += 1
        else: 
            count = 0
        if count >= 3:
            return False

    return True

def cekStrip(param):
    strip = '-'
    if strip in str(param):
        param = param.split(strip)
        for i in param:
            if len(i) == 4:
                return True
            else:
                return False
    else:
        return True

inside = open('ccNasabah.json', 'r')
out = json.load(inside)
# print(out[0]['nama'])

validDict = {}
count = 0

for i in out:
    booleanList = []
    booleanList.append(cekDepan(i['noCreditCard']))
    booleanList.append(cekPanjang(i['noCreditCard']))
    booleanList.append(cekAngka(i['noCreditCard']))
    booleanList.append(cekUlang(i['noCreditCard']))
    booleanList.append(cekStrip(i['noCreditCard']))
    booleanList.append(cekTitik(i['noCreditCard']))
    print(booleanList)
    boolCount = 0

    for i in booleanList:
        if i == True:
            boolCount += 1
        if boolCount == 6:
            validDict[count] = 1
        else:
            validDict[count] = 0
    count += 1

print(validDict)

validData = []
invalidData = []

for i in range(len(validDict)):
    if validDict[i] == 1:
        validData.append({
            'nama': out[i]['nama'],
            'noCreditCard': out[i]['noCreditCard']
        })
    else:
        invalidData.append({
            'nama': out[i]['nama'],
            'noCreditCard': out[i]['noCreditCard']
        })

with open('ccValid.json', 'w') as outfile:
    json.dump(validData, outfile)

with open('ccInvalid.json', 'w') as outfile:
    json.dump(invalidData, outfile)