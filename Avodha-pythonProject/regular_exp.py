import re
# pattern=r'avodha'
# if re.search(pattern,'helloavodha how are you'):
#     print('matched')
# else:
    # print('not matched')
# print(re.findall(pattern,'avodha hello how are avodhaavodha haiavodha'))

# ---find and replace----
# str='hai avodha how are you?'
# pattern='avodha'
# new1=re.sub(pattern,'AVODHA NEW',str)
# print(new1)

# ------matcch()------
# pattern=r'av.dha'
# if re.match(pattern,'avoodha'):
#     print('matched')
# else:
#     print('not matched')

#-----character class----

pattern=r'[a-z][A-Z][0-9]'
if re.search(pattern,'aV3'):
    print('correct')
else:
    print('not correct')