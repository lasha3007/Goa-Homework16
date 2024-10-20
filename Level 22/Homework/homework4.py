def manual_split(string, start, end, step):
    if not (0 <= start < len(string)):
        raise ValueError("Start index is out of range.")
    if not (0 <= end <= len(string)):
        raise ValueError("End index is out of range.")
    if step == 0:
        raise ValueError("Step value cannot be zero.")
    
    result = ""
    
    for i in range(start, end, step):
        result += string[i]
    
    return result

user_string = input("Enter a string: ")
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))
step = int(input("Enter the step value: "))

print(manual_split(user_string, start, end, step))
