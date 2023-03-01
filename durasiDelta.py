from datetime import datetime, timedelta

a = '0 00:56:19'
b = '912 04:17:11'
stm = b

t = datetime.strptime(stm[-8:], "%H:%M:%S")
print(t)

delta = timedelta(days=int(stm[:len(stm)-9]),hours=t.hour, minutes=t.minute, seconds=t.second)
print(delta)

print("panjang string a adalah: ", len(a))
print("panjang string a adalah: ", len(b))

s = len(a)-9
print(b[:len(b)-9])
