####LEVEL 1####
####convert str to binary output format of braille###
def solution7(s):
    ans = ''
    alp = {'a':'100000','A':'100000','b':'110000','B':'110000',
           'c':'100100','C':'100100','d':'100110','D':'100110',
           'e':'100010','E':'100010','f':'110100','F':'110100',
           'g':'110110','G':'110110','h':'110010','H':'110010',
           'i':'010100','I':'010100','j':'010110','J':'010110',
           'k':'101000','K':'101000','l':'111000','L':'111000',
           'm':'101100','M':'101100','n':'101110','N':'101110',
           'o':'101010', 'O':'101010','p':'111100','P':'111100',
           'q':'111110','Q':'111110','r':'111010','R':'111010',
           's':'011100','S':'011100','t':'011110','T':'011110',
           'u':'101001','U':'101001','v':'111001','V':'111001',
           'w':'010111','W':'010111','x':'101101','X':'101101',
           'y':'101111','Y':'101111','z':'101011','Z':'101011', 
           ' ':'000000'}           
    for i in range (len(s)):
        if s[i].isupper() == True:
            ans = ans+'000001'   
        el = alp[s[i]]
        ans = ans+el
    return ans
#print(solution7("hello"))