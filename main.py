from flask import Flask, render_template
from model import my_function
from model import my_function2
app = Flask(__name__)

'''data=(
    (1,	"PAYMENT",	9839.64,	"C1671590089",	170136,	160296.36,	"M1979787155",	0,	0,	1),
    (1,	"DEBIT",	5337.77,	"C1671590089",	41720,	36382.23,	"C195600860",	41898,	40348.79,	1,),
    (1,	"CASH_OUT",	229133.94,	"C1053967012",	15325,	0,	"C476402209",	5083,	51513.44,	0),
    (1,	"PAYMENT",	1157.86,	"C1632497828",	21156,	19998.14,	"M1877062907", 0,	0,	0),
    (1,	"PAYMENT",	671.64,	"C764826684",	15123,	14451.36,	"M473053293", 0,	0,	0),
    (1,	"TRANSFER",	215310.3,	"C2103763750",	705,	0,	"C1100439041", 22425,	0,	0),
    (1,	"PAYMENT",	1373.43,	"C215078753", 3854,	12480.57,	"M1344519051", 0,	0,	0),
    (1,	"DEBIT",	9302.79,	"C840514538",	11299,	1996.21,	"C1973538135", 29832,	16896.7,	0),
    (1,	"DEBIT",	1065.41,	"C1768242710",	1817,	751.59,	"C515132998", 10330,	0,	0),
    (1,	"PAYMENT",	3876.41,	"C247113419", 67852,	63975.59,	"M1404932042", 0,	0,	0),
    (1,	"TRANSFER",	311685.89,	"C1238616099",	10835,	0,	"C932583850", 6267,	2719172.89,	0)
)

cust=(
    "C1671590089",
    "C1053967012",
    "C1632497828",
    "C764826684",
    "C2103763750",
    "C215078753",
    "C840514538",
    "C1768242710",
    "C247113419",
    "C1238616099"
)'''
data=my_function()
cust=my_function2()

@app.route("/")
def home():
    return render_template('index.html', data=data, cust=cust)

@app.route("/test")
def filterData(custID):
    temp_data = []
    for i in data:
        print(i[3])
        if i[3] == custID:
            temp_data.append(i)
    return temp_data

@app.route("/customer/<custID>")

def about(custID):
    print(custID)
    temp_data = filterData(custID)
    print("Filtered data", temp_data)
    return render_template('customer.html', data=temp_data, custID=custID)

app.run(debug=True)

