szotar = {'A':'•-','N':'-•','0':'-----','B':'-•••','O':'---','1':'•----','C':'-•-•','P':'•--•','2':'••---','D':'-••','Q':'--•-','3':'•••--','E':'•','R':'•-•','4':'••••-','F':'••-•','S':'•••','5':'•••••','G':'--•','T':'-','6':'-••••','H':'••••','U':'••-','7':'--•••','I':'••','V':'•••-','8':'---••','J':'•---','W':'•--','9':'----•','K':'-•-','X':'-••-','.':'•-•-•-','L':'•-••','Y':'-•--',',':'--••--','M':'--','Z':'--••','?':'••--••',' ':'/'}
szotar2 = {value:key for key, value in szotar.items()}

sz = input('Adja meg a szoveget: ')
sz = sz.upper()
string = ""
if '•'==sz[0] or '-'==sz[0]:
    betu = sz.split(' ')
    for e in betu:
        # print(szotar.get(e))
        string += szotar2.get(e)
else:
    for e in sz:
        string += szotar.get(e)
        string += " "

print(string)
