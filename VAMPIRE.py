import platform,os
os.system("git pull")
bit = platform.architecture()[0]
if bit == '64bit':
    import VAMPIRE
else:
    print('SORRY THIS TOOL SUPPORT ONLY 64 BIT')
