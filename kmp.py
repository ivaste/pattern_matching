def kmp_table(W):
    n = len(W)
    T = [0 for _ in range(n)]
    T[0] = -1
    pos = 0

    for i in range(1, n):
        if W[i] == W[pos]:
            T[i] = T[pos]
        else:
            T[i] = pos
            pos = T[pos]
            while pos >= 0 and W[i] != W[pos]:
                pos = T[pos]
        pos += 1

    return T

def KMP(string, substring):
    m = len(substring)
    n = len(string)
    T = kmp_table(substring)

    pos = 0
    i = 0

    while i < n:
        if string[i] != substring[pos]:
            pos = T[pos]
            if pos < 0:
                pos += 1
                i += 1
        else:
            i += 1
            pos += 1

            if pos == m:
                return True
    return False

######################################################
window_size=4
reference_file="reference_files/rfc7252.txt"
file_to_check="files_to_check/IoT_CoAP (1).txt"

#Read reference
f = open(reference_file, "r")
text=f.read()
f.close()

#Read pattern
f = open(file_to_check, "r",encoding='utf-8')
string_to_check=f.read()
f.close()
string_to_check=string_to_check.replace("\n", " ")
string_to_check=string_to_check.split(" ")

print("Reference Text:",str(len(text.split(" "))),"words")
print("File to check:",len(string_to_check),"words")
print("Window size:",window_size,"words")

######################################################
ans=[False]*len(string_to_check)
for i in range(len(string_to_check)-window_size):
    print("Matching: "+str(100*i//len(string_to_check))+"%",end="\r", flush=True)

    pattern=" ".join(string_to_check[i:i+window_size])
    if KMP(text,pattern):
        for j in range(i,i+window_size):
            ans[j]=True

######################################################
print("Saving...")

solution=[]
for i in range(len(ans)):
    if ans[i]:
        solution.append('<span style="color: red">')
        solution.append(string_to_check[i])
        solution.append("</span>")
    else:
        solution.append(string_to_check[i])
solution=" ".join(solution)

import time
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%Y-%m-%d_%H-%M-%S", named_tuple)

f = open("solution_"+time_string+".html", "wt",encoding='utf-8')
f.write(solution)
f.close()
print("Saved")




"""
TODO:
    - load pdf and convert it to txt
    - select files from command line
    - multiple references files
    - Better pattern matching algorithm


"""