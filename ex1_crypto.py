
# Script for ciphertext a, breaking a simple shift cipher:

# ciphertext = "Yt gj, tw sty yt gj, ymfy nx ymj vzjxynts: Bmjymjw ’ynx stgqjw ns ymj rnsi yt xzkkjw Ymj xqnslx fsi fwwtbx tk tzywfljtzx ktwyzsj, Tw yt yfpj fwrx flfnsxy f xjf tk ywtzgqjx Fsi gd tuutxnsl jsi ymjr. Yt inj—yt xqjju, St rtwj; fsi gd f xqjju yt xfd bj jsi Ymj mjfwy-fhmj fsi ymj ymtzxfsi sfyzwfq xmthpx Ymfy kqjxm nx mjnw yt: ’ynx f htsxzrrfynts Ijatzyqd yt gj bnxm’i."

ciphertext = input('Type the ciphertext here:')

ciphertext = ciphertext.lower()

# print(lowered_cipher)
# print(ord("a"))
# print(ord("z"))

shifted_outputs = []
for i in range(0, 25):
    shifted_outputs.append("")
    for char in ciphertext:
        if 96 < ord(char) and ord(char) < 123:
            shifted_outputs[i]+=chr((ord(char) - 97 + (26 - i)) % 26 + 97)
        else:
            shifted_outputs[i]+=char

# print (shift_outputs[5])
for key, shifted in enumerate(shifted_outputs):
    if ("question" in shifted):
        print(f'ENCRYPTED MESSAGE IS: \n{shifted}\n')
        print(f'KEY (number of shifted letters) is: {key}')
