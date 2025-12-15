# for i in range(1, 10):
#     try:
#         print(i/(i-5))
#     except IOError:
#         print("IO not allowed.")
#     except ZeroDivisionError:
#         print("Division by zero is not allowed.")
#     except IndexError:
#         print("Index error occurred.")


# lt = [10, 20, 30, 40, 50]
# try:
#     print(lt[2]+lt[1])
# except (IOError, ZeroDivisionError, IndexError, TypeError) as e:
#     print("Error occurred:", e)
# finally:
#     print("Execution completed.")

class AgeError(Exception):
    pass

def setAge(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    elif age < 18:
        print("not legally can vote ")
    else:
        print("legally can vote ")

try:
    setAge(-5)
except AgeError as ve:
    print("AgeError:", ve)


def setAge(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        print("not legally can vote ")
    else:
        print("legally can vote ")


try:
    setAge(-5)
except ValueError as ve:
    print("AgeError:", ve)