#!/usr/bin/python3.5

from datetime import date, timedelta

# Function to create data for check
def all_day(x):
   today = date.today()
   all_day = today - timedelta(days=x)
   return all_day

# Functin for shell request
#Так не вдалось оскільки вийшов затик в процесі
def shely(command):
   import subprocess
   shely = subprocess.check_output("%s" %command, shell=True)
   return shely

# Argument 
chek_day = int(input("Set day for check  "))
name = input("Write username  ")
delimetr = "-"

# Create list with date for recheck
virt="virsh list --all | grep %s | grep off | awk '{print $2}'" %(name)
fullname=shely(virt)
ub = fullname.decode("utf-8")
ub = ub.split()

# Empety list for result 
res=[]

for i in range(chek_day):
   k = name+delimetr+str(all_day(i))
   res.append(k)

# From ub we remove res and print list VM for destroy
for l in res:
   if l in ub:
       ub.remove(l)
print("This virtuals we can destroy or delete")
print(ub)

what_do=input("If you whand delete VM please write  Y  ")
print(type(what_do))

if what_do == 'Y':
   for j in range(len(ub)):
       dest="virsh undefine %s" %(ub[j])
       print(dest)
       shely(dest)
       print("This Vm was undefined")
       print(ub[j])
else:
   print("Have a nice day!")
   print("See chenge")
