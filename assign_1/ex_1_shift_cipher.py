english_letter_freq = {
    'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.042, 'e': 0.127,
    'f': 0.022, 'g': 0.020, 'h': 0.061, 'i': 0.070, 'j': 0.001,
    'k': 0.008, 'l': 0.040, 'm': 0.024, 'n': 0.067, 'o': 0.075,
    'p': 0.019, 'q': 0.001, 'r': 0.060, 's': 0.063, 't': 0.090,
    'u': 0.028, 'v': 0.010, 'w': 0.024, 'x': 0.001, 'y': 0.020,
    'z': 0.001
}

ciphertext = "Yt gj, tw sty yt gj, ymfy nx ymj vzjxynts: Bmjymjw ’ynx stgqjw ns ymj rnsi yt xzkkjw Ymj xqnslx fsi fwwtbx tk tzywfljtzx ktwyzsj, Tw yt yfpj fwrx flfnsxy f xjf tk ywtzgqjx Fsi gd tuutxnsl jsi ymjr. Yt inj—yt xqjju, St rtwj; fsi gd f xqjju yt xfd bj jsi Ymj mjfwy-fhmj fsi ymj ymtzxfsi sfyzwfq xmthpx Ymfy kqjxm nx mjnw yt: ’ynx f htsxzrrfynts Ijatzyqd yt gj bnxm’i."

# ciphertext_13_shifted
# ciphertext = "Gb or, be abg gb or, gung vf gur dhrfgvba: Jurgure ’gvf aboyre va gur zvaq gb fhssre Gur fyvatf naq neebjf bs bhgentrbhf sbeghar, Be gb gnxr nezf ntnvafg n frn bs gebhoyrf Naq ol bccbfvat raq gurz. Gb qvr--gb fyrrc, Ab zber; naq ol n fyrrc gb fnl jr raq Gur urneg-npur naq gur gubhfnaq angheny fubpxf Gung syrfu vf urve gb: ’gvf n pbafhzzngvba Qribhgyl gb or jvfu’q."

# random text from net, shifted 17 letters
# ciphertext = "Kyv ljv fw “jrdgcv kvok” zj hlzkv tfddfe ze mrizflj zeuljkizvj, wifd uvjzxe reu glsczjyzex kf vultrkzfe reu jfwknriv uvmvcfgdvek. Nyvkyvi pfl’iv kvjkzex r crpflk, wfidrkkzex r uftldvek, fi cvriezex r evn crexlrxv, jrdgcv kvok ze Vexczjy gcrpj r tiltzrc ifcv ze vejlizex hlrczkp reu wletkzferczkp. Kyzj rikztcv nzcc vogcfiv nyrk “jrdgcv kvok” zj, zkj rggcztrkzfej, reu kyv zdgfikretv fw ljzex zk vwwvtkzmvcp."

# ciphertext = input('Type the shifted message here:')

ciphertext = ciphertext.lower()

def compute_letter_frequency(text):
    frequency_dict = {chr(i): 0 for i in range(97, 123)}
    letters_total = 0
    for letter in text:
        if 96 < ord(letter) and ord(letter) < 123:
            # print(f'current letter from ciphertext: {letter}')
            # print(f'frequency_dict[{letter}]+=1')
            frequency_dict[letter]+=1
            letters_total+=1
    for letter in frequency_dict:
        frequency_dict[letter] = frequency_dict[letter]/letters_total
    return frequency_dict

shifted_texts = []
for i in range(0, 25):
    shifted_texts.append("")
    for char in ciphertext:
        if 96 < ord(char) and ord(char) < 123:
            shifted_texts[i]+=chr((ord(char) - 97 + (26 - i)) % 26 + 97)
        else:
            shifted_texts[i]+=char

all_shifted_texts_stat_distance = []

stat_distances = []
print(f'k       |   delta(english, shifted)\n')
for shifted_text in shifted_texts:
    # all_shifted_letter_frequencies.append(compute_letter_frequency(shifted_text))
    stat_distance = 0
    for letter in english_letter_freq:
        shifted_text_letter_freq = compute_letter_frequency(shifted_text)
        if shifted_text_letter_freq[letter] > 0:
            stat_distance += 0.5 * abs(english_letter_freq[letter] - shifted_text_letter_freq[letter])
    stat_distances.append(stat_distance)
    print(f'{shifted_texts.index(shifted_text)}       |   {stat_distance}')

# print(stat_distances.index(min(stat_distances)))

print(f'\n\nENCRYPTION KEY:\n{stat_distances.index(min(stat_distances))}')

print(f'\n\nDECRPYTED MESSAGE:\n{shifted_texts[stat_distances.index(min(stat_distances))]}')
