D = input()
oc,of,od = input().split()
cs,cb,cm,cd =  input().split()
ocost = 0
ccost = 0
ocost= int(oc) + (int(D)-int(of))*int(od)
ccost = int(cb) + (int(D)/int(cs))*int(cm) + int(D)*int(cd) 
if ocost>ccost:
    print( 'Classic Taxi')
else:
    print( 'Online Taxi')
