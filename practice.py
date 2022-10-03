try:
    print("divide a calculator")
    nums = []
    nums.append(int(input("1st number")))
    nums.append(int(input("2nd number")))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("Error! warning not number")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("I don't know this Error!")
    print(err)