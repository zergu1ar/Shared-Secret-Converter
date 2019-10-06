import json
import uuid
import biplist
import sys

filename = sys.argv[1]
try:
    pl_file = biplist.readPlist(filename)
except biplist.InvalidPlistException:
    print('[!] Can\'t open Steamguard file')
    exit(0)
data_array = {}
for i in range(2, 14):
    data_array[pl_file.get('$objects')[i]] = pl_file.get('$objects')[12+i]
data_array['device_id'] = 'android:' + str(uuid.uuid4())
data_array['fully_enrolled'] = True
data_array['Session'] = {}
data_array['Session']['SessionID'] = ''
data_array['Session']['SteamLogin'] = ''
data_array['Session']['SteamLoginSecure'] = ''
data_array['Session']['WebCookie'] = None
data_array['Session']['OAuthToken'] = ''
data_array['Session']['SteamID'] = data_array['steamid']
del data_array['steamguard_scheme'], data_array['steamid']
result = open(data_array['account_name'] + '.maFile', 'w')
result.write(json.dumps(data_array))
result.close()
print('[+] Success: ' + filename + ' => ' + data_array['account_name'] + '.maFile')
exit(0)
