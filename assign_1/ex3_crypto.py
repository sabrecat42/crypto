import math

# Sets of plaintexts, keys, and ciphertexts
M = ['a', 'b', 'c', 'd']  # Plaintexts
K = ['k1', 'k2', 'k3', 'k4']  # Keys
C = [1, 2, 3, 4]  # Ciphertexts

# Probabilities for plaintexts
Pr_M = {
    'a': 1/3,
    'b': 4/15,
    'c': 1/5,
    'd': 1/5
}

# Probabilities for keys
Pr_K = {
    'k1': 1/5,
    'k2': 3/10,
    'k3': 1/5,
    'k4': 3/10
}

# Encryption scheme as a dictionary of dictionaries
encryption_scheme = {
    'k1': {'a': 3, 'b': 1, 'c': 4, 'd': 2},
    'k2': {'a': 2, 'b': 4, 'c': 1, 'd': 3},
    'k3': {'a': 4, 'b': 2, 'c': 3, 'd': 1},
    'k4': {'a': 1, 'b': 3, 'c': 2, 'd': 4}
}

# (a) (3 points) Calculate the probability of each plaintext conditioned on each ciphertext occurrence.

# We need p(P = m | C = c) for each m in M and c in C.
# Use Bayes Theorem to rewrite p(P = m | C = c) as (p(P = m) * p(C = c | P = m)) / P (C = c)

# To be able to apply the Bayes Theorem, we first need to compute:
#   1: P(C=c) for each ciphertext
#   2: all the probabilities where c is the ciphertext given that m is the plaintext (i.e. p(C = c | P = m))

# 1: Computing each P(C=c)
Pr_C = {}

for ciphertext in C:
    print(f'Computing p(C={ciphertext})')
    pr_ciphertext = 0
    for encryption_k in encryption_scheme:
        print(f'    Computing for encryption: {encryption_k}')
        for plain_t, cypher_t in encryption_scheme[encryption_k].items():
            if cypher_t == ciphertext:
                print(f'        P(C={ciphertext}) += {Pr_K[encryption_k]} * {round(Pr_M[plain_t], 2)}')
                pr_ciphertext += Pr_K[encryption_k] * Pr_M[plain_t]
    Pr_C.update({ciphertext: pr_ciphertext})

print("\n")
# for c, pr_c in enumerate(Pr_C):
#     print(f'P(C={c+1}) = {round(pr_c, 4)}')
for c in Pr_C:
    print(f'P(C={c}) = {round(Pr_C[c], 4)}')
print("\n")

print(f'{Pr_C}\n\n')

# 2: Computing all the probabilities where c is the ciphertext given that m is the plaintext (i.e. p(C = c | P = m))

Pr_C_given_M = {}

for plaintext in M:
    Pr_C_given_M[plaintext] = {}
    for ciphertext in C:
        pr_c_given_m = 0
        print (f'Computing P(C={ciphertext}|P={plaintext}):')
        for encryption_k in encryption_scheme:
            for plain_t, cypher_t in encryption_scheme[encryption_k].items():
                if plain_t == plaintext and cypher_t == ciphertext:
                    print(f'    P(C={ciphertext}|P={plaintext}) += P(K={encryption_k})  [{Pr_K[encryption_k]}]')
                    pr_c_given_m += Pr_K[encryption_k]
        Pr_C_given_M[plaintext].update({ciphertext: pr_c_given_m})
        
# print(Pr_C_given_M)
print('\n')
for m in Pr_C_given_M:
    for c in Pr_C_given_M[m]:
        print(f'P(C={c}|P={m}) = {Pr_C_given_M[m][c]}')
    print('\n')

# Finally, compute the probability of each plaintext conditioned on each ciphertext occurrence P(m|c) using Bayes Theorem

print('Computing P(m|c):')

Pr_M_given_C = {}
for ciphertext in C:
    # pr_m_given_c = 0
    # print (f'Computing P(P={plaintext}|C={ciphertext}):')
    Pr_M_given_C[ciphertext] = {}
    for plaintext in M:
        pr_m_given_c = (Pr_C_given_M[plaintext][ciphertext] * Pr_M[plaintext]) / Pr_C[ciphertext]
        print(f'    P(P={plaintext}|C={ciphertext}) = ({round(Pr_C_given_M[plaintext][ciphertext], 4)} * {round(Pr_M[plaintext],4)})/ {round(Pr_C[ciphertext], 4)} = {round(pr_m_given_c, 4)}')
        Pr_M_given_C[ciphertext].update({plaintext: pr_m_given_c})
    print('\n')

# print(Pr_M_given_C)
print('\n')
for c in Pr_M_given_C:
    pr_sum = 0
    for m in Pr_M_given_C[c]:
        print(f'P(P={m}|C={c}) = {round(Pr_M_given_C[c][m], 4)}')
        pr_sum += Pr_M_given_C[c][m]
    print()
    print('\n')

# (b) (3 points) Compute the entropy value for H(M |C).
# To compute H(M|C), we will apply the formula for entropy of a plaintext (M) given a ciphertext (C).
# We will use the entropy of M given an observation of Y=y first:
# H(M \mid C = c) = - \sum_{m} p(M = m \mid C = c) \cdot \log_2 p(M = m \mid C = c).
# For H(M \mid C) = - \sum_{m} \sum_{c} p(C = c) \cdot p(M = m \mid C = c) \cdot \log_2 p(M = m \mid C = c).

En_M_given_C = 0

for c in C:
    En_M_given_c = 0
    for m in M:
        En_M_given_C -= Pr_C[c] * Pr_M_given_C[c][m] * math.log(Pr_M_given_C[c][m], 2)
        En_M_given_c -= Pr_C[c] * Pr_M_given_C[c][m] * math.log(Pr_M_given_C[c][m], 2)
        
        print(f'\nFor M={m}, C={c}')
        print(f'    E(M|C) -= Pr(C={c}) * P(M={m}|C={c}) * log(P(M={m}|C={c})')
        print(f'    E(M|C) -= {round(Pr_C[c],4)} * {round(Pr_M_given_C[c][m],4)} * {round((math.log(Pr_M_given_C[c][m], 2)),4)}')
        print(f'    E(M|C) += {-round((Pr_C[c] * Pr_M_given_C[c][m] * math.log(Pr_M_given_C[c][m], 2)),4)}')
    print(f'\nP(M|C={c})={round(En_M_given_c, 4)}')

print(f'\nH(M|C) = {round(En_M_given_C, 4)}\n')

# The resulting entropy represents the amount of information about the plaintext given a ciphertext.
# If it is much lower than the entropy of a plaintext, then the ciphertext reveals much information about the plaintext, meaning the
# scheme is unsecure. For reference, the entropy of a plaintext for this scheme is H(M) = 1.9656 vs H(M|C) = 1.9367.

En_M = 0
for m in M:
    En_M -= Pr_M[m] * math.log(Pr_M[m],2)
print(f'For reference: H(M) = {round(En_M, 4)}')

# (c) (2 points) Is this scheme perfectly secure? Explain briefly.
# A scheme to be perfectly secure if and only if:
# a. every key is used with equal probability
# b. For each plaintext and ciphertext, there is a unique key k such that encrypting the plaintext m you obtain the ciphertext c.
# 
# In our case, the scheme is not prefectly secure because, even though condition b is satisfied,
# the probabilities for each of the keys are not equal (e.g. P(K=k1)=1/5 and P(K=k2)=3/10 -> P(K=k1) <> P(K=k2)).
