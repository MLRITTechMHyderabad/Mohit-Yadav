def merging_dict(dict1, dict2):
    ans = dict1.copy()  

    for key, value in dict2.items():
        if key in ans:
      
            if isinstance(ans[key], list):
                ans[key].append(value)
            else:
                ans[key] = [ans[key], value]  
        else:
            ans[key] = [value]  

    return ans


dict1 = {"name1": ["Alice"], "age1": [25], "city1": ["New York"]}
dict2 = {"name1": "Bob", "age1": 30, "city1": "Los Angeles"}


print(merging_dict(dict1, dict2))
