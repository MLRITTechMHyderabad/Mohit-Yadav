def process_data(data, index):
    pass
    try:
        IntData = [int(x) for x in data]
        result = IntData[index] / IntData[index - 1]
        return result 
    except ZeroDivisionError:
        return "Division by zero Error"
    except ValueError:
        return "Value Error"
    except IndexError:
        return "Index out of bounds"
    except Exception as e:
        return e
data_list = ["10", "20", "0", "40"]
print(process_data(data_list, 3))
print(process_data(["10", "abc", "30"], 1))
print(process_data([10, 20], 5))