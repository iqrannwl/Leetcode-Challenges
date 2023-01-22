class Solution:
    def romanToInt(self,s:str)->int:
        length = len(s)
        mydictionary = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        if length == 1:
            return mydictionary[s[0]]
        else:
            ans = mydictionary[s[0]]
            for i in range(1,length):
                if mydictionary[s[i]] > mydictionary[s[i-1]]:
                    ans +=mydictionary[s[i]] - (2*mydictionary[s[i-1]])
                else:
                    ans +=mydictionary[s[i]]
            return ans

# s = "III" 
# s = "LVIII"
s = "MCMXCIV"
myobj = Solution()
print(myobj.romanToInt(s))

