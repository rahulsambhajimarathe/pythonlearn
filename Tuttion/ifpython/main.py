# marks = 65;

# if marks >= 50:
#     print("Pass")
# else:
#     print("Fail")


working = 20
abs = 14

#sales
sales = 2000
purchase = 1500
other = 1000

basic = working*other

dept ="sales"



if dept == "sales":
    if abs >= 7:
        deducation = abs * 1000
        basic = working *sales
    elif abs >= 5:
        deducation = abs * 700
        basic = working *sales
    elif abs >= 2:
        deducation = abs * 100
        basic = working *sales
    else:
        deducation = abs * 0
        basic = working *sales
    
elif dept == "purchase":
    if abs >= 7:
        deducation = abs * 500
        basic = working *purchase
    elif abs >= 5:
        deducation = abs * 300
        basic = working *purchase
    elif abs >= 2:
        deducation = abs * 100
        basic = working *purchase
    else:
        deducation = abs * 0
        basic = working *purchase

# hra
#basic = working * sales
#basic1 = working * purchase
#otherbasic = working * other

if dept == "sales" and basic >= 20000:
    hra = basic * 5 / 100
elif dept == "purchase" and basic >= 20000:
    hra = basic * 8 /100
else:
    hra = basic * 3 / 100


#da

if dept == "sales" and working >= 25:
    da =basic*3/100
else:
    da = basic*5/100


if dept == "sales":
    if working >= 25:
        ea = 3000
    elif working >= 20:
        ea = 2000
elif dept == "purchase":
    if working >= 25:
        ea = 2500
    elif working >= 20:
        ea = 1800
else:
    ea = 1000

#pf
# print(ea)

# if dept == "sales":
#     if working >= 25:
#         dedpf=basic*8/100
# else:
#     dedpf=basic*5/100
    
#gip

if working > 20:
    gip = 3000
elif working >= 15 and working <= 20:
    gip = 2000
else:
    gip = 1000
    



print(td)