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

import sys
import glob

window_size=4

print(sys.argv)

#Get files paths from command line
if len(sys.argv)!=3:
    print("Insert file_to_check reference_files_directory")
    sys.exit(1)

file_to_check=sys.argv[1]

reference_files=[]
reference_files_directory=sys.argv[2]
for file in glob.glob(reference_files_directory+'/*'):
    reference_files.append(file)


#Read pattern
f = open(file_to_check, "r",encoding='utf-8')
string_to_check=f.read()
f.close()
string_to_check=string_to_check.replace("\n", " ")
string_to_check=string_to_check.lower()
string_to_check=string_to_check.split(" ")


print("File to check:",len(string_to_check),"words")
print("Window size:",window_size,"words")


######################################################
ans=[False]*len(string_to_check)

#for each reference file
for i in range(len(reference_files)):
    reference_file=reference_files[i]

    #Read reference file
    f = open(reference_file, "r",encoding='utf-8')
    text=f.read().lower()
    f.close()

    print("Reference Text "+str(i)+":",str(len(text.split(" "))),"words")
    for i in range(len(string_to_check)-window_size):
        print("\tMatching: "+str(100*i//len(string_to_check))+"%",end="\r", flush=True)

        pattern=" ".join(string_to_check[i:i+window_size])
        if KMP(text,pattern):
            for j in range(i,i+window_size):
                ans[j]=True


print(str(round(100*sum(ans)/len(ans),2))+"% ("+str(sum(ans))+"/"+str(len(ans))+" words) of document match, with windw size="+str(window_size),flush=True)

######################################################
#Save solution
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

file_name=file_to_check.split("/")[-1]

save_path="solution/"+file_name+"_"+time_string+".html"
f = open(save_path, "wt",encoding='utf-8')
f.write(solution)
f.close()
print("Saved to "+save_path)




"""
TODO:
    - load pdf and convert it to txt
    - select files from command line
    - Better pattern matching algorithm: https://www.toptal.com/algorithms/aho-corasick-algorithm
    - remove non standard ascii chars
    - change output directory
    - load automatically files_to_check


"""