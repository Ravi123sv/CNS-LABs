from collections import Counter

english_freq = {
    'a':8.167,'b':1.492,'c':2.782,'d':4.253,'e':12.702,'f':2.228,'g':2.015,
    'h':6.094,'i':6.966,'j':0.153,'k':0.772,'l':4.025,'m':2.406,'n':6.749,
    'o':7.507,'p':1.929,'q':0.095,'r':5.987,'s':6.327,'t':9.056,'u':2.758,
    'v':0.978,'w':2.360,'x':0.150,'y':1.974,'z':0.074
}

def score(text):
    c = Counter(text)
    total = sum(c.values())
    s = 0
    for ch in english_freq:
        obs = c.get(ch,0)/total*100
        s += abs(obs-english_freq[ch])
    return s

def decrypt(cipher,shift):
    return ''.join(chr(((ord(c)-97-shift)%26)+97) if c.isalpha() else c for c in cipher)

def attack(cipher,topn=10):
    results=[]
    for shift in range(26):
        pt=decrypt(cipher,shift)
        results.append((score(pt),shift,pt))
    results.sort(key=lambda x:x[0])
    return results[:topn]

if __name__=="__main__":
    cipher="wklv lv d whvw phvvdjh"  # example ciphertext
    top=attack(cipher,10)
    for s,shift,pt in top:
        print(f"Shift {shift}: {pt}")
