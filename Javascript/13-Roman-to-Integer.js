var romanToInt = function(s) {
    var myobj = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    if(s.length == 1){
        return myobj[s[0]]
    }
    else{
        let ans = myobj[s[0]]
        for(let i=1; i<s.length; i++){
            if(myobj[s[i]] >  myobj[s[i-1]]){
                ans += myobj[s[i]] - (myobj[s[i-1]]*2)
            }
            else{
                ans +=myobj[s[i]]
            }
        }
        return ans
    }
};

//let  s = "III" 
//let  s = "LVIII"
let s = "MCMXCIV"
let result=romanToInt(s)
console.log(result)