def lenght(val):

    print("\nMeasurement Types:\nmm  |  cm  |  m  |  km")

    input_unit  = input("\nChoose your input measturement type:")
    output_unit = input("\nChoose your output measturement type:")
    UNITS = {'mm':0.001,'cm':0.01,'m':1.0,'km':1000.}
    result = val*UNITS[input_unit]/UNITS[output_unit]
    #result = int(result)
    msg = f'\nResult : {result}'
    print(msg + output_unit)


def weight(val2):

    print("\nWeight Types:\nmg  |  g  |  kg  |  ton")

    input_unit  = input("\nChoose your input measturement type:")
    output_unit = input("\nChoose your output measturement type:")
    UNITS = {'mm':0.000001,'g':0.001,'kg':1.0,'ton':1000.}
    result = val2*UNITS[input_unit]/UNITS[output_unit]
    #result = int(result)
    msg = f'\nResult : {result}'
    print(msg + output_unit)

def power():
    print("power")

def temp():
    print("temp")

def area():
    print("area")

def volume():
    print("volume")

def time():
    print("time")

def pressure():
    print("pressure")

def data():
    print("data")