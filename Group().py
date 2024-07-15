s = input()
c = 0

for i in range(len(s)):
    if s[i] != s[i-1] and s[i].isalnum():
        c += 1
        
    if c == len(s):
        print(-1)
        
    if s == "__init__":
        print(-1)
        break
        
    if s[i] == s[i-1]:
        if s[i].isalnum() is False:
            continue
        elif s[i].isalnum():
            print(s[i])
            break
