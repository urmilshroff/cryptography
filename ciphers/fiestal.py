p_list = []
plain_text = list(input("Enter binary text:\n"))
key = int(input("Enter key:\n"))

p_box=[31, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 20, 21, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 19, 31, 31, 31, 1]

for i in range(31):
    p_list.append(plain_text[p_box[i]])
    
print(p_list)