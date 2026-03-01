from arc4 import ARC4
ENCRYPTED_CHIMERA_FORMULA=b'r2b-\r\x9e\xf2\x1fp\x185\x82\xcf\xfc\x90\x14\xf1O\xad#]\xf3\xe2\xc0L\xd0\xc1e\x0c\xea\xec\xae\x11b\xa7\x8c\xaa!\xa1\x9d\xc2\x90'
current_user=b'G0ld3n_Tr4nsmut4t10n'
arc4_decipher = ARC4(current_user)
decrypted_formula = arc4_decipher.decrypt(
                ENCRYPTED_CHIMERA_FORMULA
            ).decode()
print(decrypted_formula)
