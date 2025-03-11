# # import subprocess

# # # Run a command and capture the output
# # # result = subprocess.run(['echo', 'Hello, World!'], capture_output=True, text=True)
# # # print(result.stdout)  # Output the result: Hello, World!


# # try:
# #     subprocess.check_call(['dir'], shell=True)
# #     print('SUCCESS')
# # except subprocess.CalledProcessError:
# #     print("Command failed!")
# import subprocess

# def beginner_level():
#     def one():
#         output = subprocess.run(['echo', "Hello from subprocess!"], text=True,shell=True, capture_output=True)
#         print(output.stdout)

#         output2 = subprocess.run(['python', 'run', 'new_test.py'], text=True, capture_output=True)
#         print(output2.stdout)

#     def two():
#         output = subprocess.check_output(['dir'], text=True, shell=True)
#         listed_ouput = (output.split("\n"))

#         for line in listed_ouput:
#             print(line)
    
#     def three():
#         output2 = subprocess.run(['python', '--version'], text=True, capture_output=True)
#         print(output2.stdout)

#     def four():
#         try:
#             subprocess.check_call(['dir', 'nonexistent_folder'], shell=True)
#         except subprocess.CalledProcessError as e:
#             print(f"Command failed: {e}")

#     four()
# if __name__ == "__main__":
#     print('Hello World')
#     beginner_level()

from sys import version_info

print(version_info)