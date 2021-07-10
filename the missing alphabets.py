import string
stri_input=input()
miss_alp=""
for ele in string.ascii_lowercase:
    if ele not in stri_input:
        miss_alp+=ele
print(miss_alp)
