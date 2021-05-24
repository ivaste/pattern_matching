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



reference_file="rfc7552.txt"
file_to_check=""

#Read reference
f = open(reference_file, "r")
text=f.read()
f.close()

#Read pattern
f = open(file_to_check, "r")
string_to_check=f.read()
f.close()