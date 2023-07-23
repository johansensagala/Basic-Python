buah1 = ["mangga", "apel", "jeruk", "rambutan"]
buah2 = ["anggur", "stroberi", "ceri"]
buah3 = ["langsat", "durian", "pisang"]

print(buah1)
print(buah2)
print(buah3)

# gabung ke list

list_buah = buah1.copy() + buah2.copy() + buah3.copy()

print(list_buah)

# gabung ke dictionary

dict_buah = {
    "buah1": buah1.copy(),
    "buah2": buah2.copy(),
    "buah3": buah3.copy()
}

print(dict_buah)