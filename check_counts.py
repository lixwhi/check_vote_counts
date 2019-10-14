from web3 import Web3
import json
import time
web3 = Web3(Web3.HTTPProvider('http://192.168.0.24:8545'))

ETH_SCALE = 1000000000000000000

CHIEF = '0x9eF05f7F6deB616fd37aC3c959a2dDD25A54E4F5'

STORAGE_ADDRESS_175 = '0x7194895226521b264c1718437ceee76a2bdd3063d5d78c0d9ba690edeb922c53'
STORAGE_ADDRESS_185 = '0x1f42fd789e1fb5d34f365215219111a9335ed0911da620de3fd9992f9e5900bf'
STORAGE_ADDRESS_205 = '0xf55ab75f9089ec31ac3e2fd408a16fe9ddd50e8d8bfcb7aa7e97eaa8377e0792'
STORAGE_ADDRESS_225 = '0x079ea8688746ca3c039cc6de83b7c3e9df4c124fea469195aabdd2fea424b500'
STORAGE_ADDRESS_205_2 = '0x0046bdd073d32cf493f29ea4ba521cee6bc0b69a95a421858c63673bfcc728cc'
STORAGE_ADDRESS_185_2 = '0x4b9ba0f07c934da097d0ec612d9a376d17fc679d69b2d3d42d99c14d4e567c44'
STORAGE_ADDRESS_165 = '0xd18793a9cf093b47b9f75519e4bb2eeea28aaecbb3cc3433cd3e524417707cf5'
STORAGE_ADDRESS_145 = '0x8012753d7729c8b849a362fda441de5380dcb4758e0a4d2f59607b00add5fabb'
STORAGE_ADDRESS_125 = '0xac37e5a50d5e68c5c43515709d42e3a685dae5012e13e0ae350c161cc639f093'
STORAGE_ADDRESS_105 = '0x210a49d694d555987a17563881a3308d8340bb0c211155c36824502dfdf96ea1'
STORAGE_ADDRESS_085 = '0x90113e0968cfaec39ca650108d1ec56b7e6c69807c85234783656d4b51c5e07b'
STORAGE_ADDRESS_095 = '0xf77c58966018b73304e3ca12619387209c5176aa9db117e9d8676d27aa101a4e'


CHIEF_ABI = json.loads('[{"constant":true,"inputs":[],"name":"IOU","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"getUserRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"GOV","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"getCapabilityRoles","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"isCapabilityPublic","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_YAYS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"whom","type":"address"}],"name":"lift","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"etch","outputs":[{"name":"slate","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"approvals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"},{"name":"enabled","type":"bool"}],"name":"setUserRole","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"role","type":"uint8"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setRoleCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"},{"name":"role","type":"uint8"}],"name":"hasUserRole","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"slate","type":"bytes32"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"caller","type":"address"},{"name":"code","type":"address"},{"name":"sig","type":"bytes4"}],"name":"canCall","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"},{"name":"","type":"uint256"}],"name":"slates","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"code","type":"address"},{"name":"sig","type":"bytes4"},{"name":"enabled","type":"bool"}],"name":"setPublicCapability","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"who","type":"address"},{"name":"enabled","type":"bool"}],"name":"setRootUser","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"votes","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"free","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"lock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"yays","type":"address[]"}],"name":"vote","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"isUserRoot","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"deposits","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"hat","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"GOV","type":"address"},{"name":"IOU","type":"address"},{"name":"MAX_YAYS","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"slate","type":"bytes32"}],"name":"Etch","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"}]')

chief_contract = web3.eth.contract(address=CHIEF, abi=CHIEF_ABI)

def main():
	previous_bn = web3.eth.blockNumber
	while (True):
		current_bn = web3.eth.blockNumber
		if (previous_bn != current_bn):
			previous_bn = current_bn
			print('\nchecking block {0}'.format(current_bn))
			
			
			count_205_2 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_205_2))))[2:66].lstrip('0'), 16)
			count_185_2 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_185_2))))[2:66].lstrip('0'), 16)
			count_165 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_165))))[2:66].lstrip('0'), 16)
			count_145 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_145))))[2:66].lstrip('0'), 16)
			count_125 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_125))))[2:66].lstrip('0'), 16)
			count_105 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_105))))[2:66].lstrip('0'), 16)
			count_085 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_085))))[2:66].lstrip('0'), 16)
			count_095 = int(web3.toHex(bytes(web3.eth.getStorageAt(CHIEF, web3.toInt(hexstr=STORAGE_ADDRESS_095))))[2:66].lstrip('0'), 16)

			print('20.5 count: {0}'.format(count_205_2 / ETH_SCALE))
			print('18.5 count: {0}'.format(count_185_2 / ETH_SCALE))
			print('16.5 count: {0}'.format(count_165 / ETH_SCALE))
			print('14.5 count: {0}'.format(count_145 / ETH_SCALE))
			print('12.5 count: {0}'.format(count_125 / ETH_SCALE))
			print('10.5 count: {0}'.format(count_105 / ETH_SCALE))
			print('08.5 count: {0}'.format(count_085 / ETH_SCALE))
			print('09.5 count: {0}'.format(count_095 / ETH_SCALE))

		time.sleep(10)


if __name__ == "__main__":
	main()
