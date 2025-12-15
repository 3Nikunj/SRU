# import threading


# def square(side_length):
#     print(side_length * side_length)


# def cube(side_length):
#     print(side_length * side_length * side_length)


# # Thread for square calculation
# t1 = threading.Thread(target=square, args=(5,))
# t2 = threading.Thread(target=cube, args=(5,))    # Thread for cube calculation

# t1.start()  # Start the square thread
# t2.start()  # Start the cube thread
# t1.join()   # Wait for the square thread to finish
# t2.join()   # Wait for the cube thread to finish

# print("Done!")


from concurrent.futures import ThreadPoolExecutor
import threading


def printing(num, tnum):
    for i in range(1, num):
        print("i =", i, "thread number:", tnum)


t1 = threading.Thread(target=printing, args=(1000, 1))
t2 = threading.Thread(target=printing, args=(1000, 2))
t1.start()
t2.start()

# with ThreadPoolExecutor(max_workers=10) as executor:
#     executor.submit(printing, 1000, 1)
#     executor.submit(printing, 1000, 2)
#     executor.submit(printing, 1000, 3)
#     executor.submit(printing, 1000, 4)
