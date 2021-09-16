#main file for github data module
print ()
print ("The stuff under this message is all from an imported module.")

import Github_data_module

cool1 = Github_data_module.a
cool2 = Github_data_module.b
cool3 = Github_data_module.c
cool4 = Github_data_module.d
cool5 = Github_data_module.e
cool6 = Github_data_module.f

print ("Here is some of the numbers from the module")
print (cool1, cool2, cool3, cool4, cool5, cool6)
print (cool1, "+", cool2, "=", cool1 + cool2)
print (cool4, "-", cool6, "=", cool4 - cool6)
print (cool2, "x", cool3, "x", cool5, "=", cool2*cool3*cool5)
