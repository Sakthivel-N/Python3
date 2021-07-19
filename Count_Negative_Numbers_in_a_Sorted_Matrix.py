input_string = input()
replaced_string = input_string.replace("#"," ")
test_string = replaced_string.split(" ")
output_string = [int(element) for element in test_string if int(element) < 0]
print(len(output_string))
