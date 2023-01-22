def roman_to_int(s)
    myhash = {"I"=>1,"V"=>5,"X"=>10,"L"=>50,"C"=>100,"D"=>500,"M"=>1000}
    if s.length() == 1
        return myhash[s[0]]
    else
        ans = myhash[s[0]]
        for i in 1..(s.length()-1) do 
            if myhash[s[i]] > myhash[s[i-1]] 
                ans += myhash[s[i]] - (myhash[s[i-1]]*2)
            else 
                ans +=myhash[s[i]]
            end
        end
    return ans
    end
end

#  s = "III" 
#  s = "LVIII"
s = "MCMXCIV"
result =roman_to_int(s)
puts result