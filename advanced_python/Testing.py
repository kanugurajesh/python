# hello = ["shiva","mahadev","rudra","veerasen"]
# vishwa = ["rudra","veerasen"]
# for items in vishwa:
#     if (items in hello) == True:
#         print(items.capitalize())

# for i in range(10):
#     for j in range(10):
#         print(j,i)
h = ["shiva", "rudra","mahadev","mahaveer","tejaroopa"]
dictionary_files = ["shiva", "rudra"]
for items in dictionary_files:
    for heroes in h:
        if items == heroes:
            h.remove(items)
            print(items+"i")
        else:
            print('shiva')            
print(h)