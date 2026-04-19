global_var=10
def my_fxn():
    local_var=20
    print(global_var)
    print(local_var)
my_fxn()
print(global_var)
#local var wont print ...t will show error    