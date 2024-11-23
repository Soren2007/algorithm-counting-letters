"""
Created By SOREN SHAMLOU

Create At : 2024/11/23

Update At : ----/--/--

"""

intro = r"""
   _____  ____  _____  ______ _   _ 
  / ____|/ __ \|  __ \|  ____| \ | |
 | (___ | |  | | |__) | |__  |  \| |
  \___ \| |  | |  _  /|  __| | . ` |
  ____) | |__| | | \ \| |____| |\  |
 |_____/ \____/|_|  \_\______|_| \_|
 """

print(intro)

string = input("String >>> ")

count = {}
for char in string:
    try:
        count[f"{char}"]+=1
    except KeyError:
        count[f"{char}"]=1
for k,v in count.items():
    print(f"{k}:{v}", end=", ")