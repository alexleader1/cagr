
# Making up a Compound Annual Growth Rate (CAGR) calculator




# CAGR = (Vfinal / Vbegin) ** (1/t) - 1


# vfinal = float(input('Enter final value:\n'))
# vbegin = float(input('Enter beginning value:\n'))
# t = float(input('Enter number of periods:\n'))
#
#
#
# cagr = round(((vfinal / vbegin) ** (1 / t) - 1) * 100,2)
#
# print(f"CAGR: {cagr} %")
#

print("git practice 20240301")
print("version 1")

quit()



# ------------------------------------

# CAGR = (vfinal / vbegin) ** (1/t) - 1


vfinal = float(input('Enter final value:\n'))
vbegin = float(input('Enter beginning value:\n'))
t = float(input('Enter number of periods:\n'))


cagr = round(((vfinal / vbegin) ** (1 / t) - 1) * 100, 2)

print(f"The CAGR is {cagr} %")
