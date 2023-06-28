# Zyxel LTE5366-M206
# https://support.zyxel.eu/hc/en-us/articles/4403349814802-Advanced-Downloads-for-LTE-devices
# From the /usr/sbin/commander that calls a bash-script genpass-ZyXEL.sh
import hashlib
import argparse

def lte5366(serial):
	md5_1_digest = hashlib.md5()
	md5_1_digest.update(serial.encode())
	md5_1_hex = md5_1_digest.hexdigest()

	ords = [ord(i) for i in md5_1_hex]
	xor_results = [i ^ 90 for i in ords]

	new_seed = "".join([chr(i) for i in xor_results]) + "Z"

	md5_2_digest = hashlib.md5()
	md5_2_digest.update(new_seed.encode())
	md5_2_hex = md5_2_digest.hexdigest()
	md5_3_digest = hashlib.md5()
	md5_3_digest.update(md5_2_hex.encode())
	md5_3_hex = md5_3_digest.hexdigest()

	str1 = md5_3_hex[5:11]
	str2 = md5_3_hex[6:13]
	
	key = str1+str2
	key = key.upper()
	print(key)


parser = argparse.ArgumentParser(description='Zyxel LTE5366-M206 Keygen')
parser.add_argument('serial', help='Serial Number')
args = parser.parse_args()

lte5366(args.serial)
