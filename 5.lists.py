list_of_sweets = ['halva', 'gulab jamun', 'kaju katli', 'peda']

print(type(list_of_sweets))

print(list_of_sweets[0])
print(list_of_sweets[-1])
print(list_of_sweets[-2])
# if need middle two then
print(list_of_sweets[1:3]) # ['gulab jamun', 'kaju katli']
print(list_of_sweets[:3]) # ['halva', 'gulab jamun', 'kaju katli']
print(list_of_sweets[:]) # ['halva', 'gulab jamun', 'kaju katli', 'peda']
print(len(list_of_sweets)) # 4 
print(list_of_sweets[-3:]) # ['gulab jamun', 'kaju katli', 'peda']
list_of_sweets.append('laddu')
print(list_of_sweets) # ['halva', 'gulab jamun', 'kaju katli', 'peda', 'laddu']
list_of_sweets.insert(2, 'rasmalai')
print(list_of_sweets) # ['halva', 'gulab jamun', 'rasmalai', 'kaju katli', 'peda', 'laddu']
dir(list_of_sweets)