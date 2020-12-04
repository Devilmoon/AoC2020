with open("input.txt") as f:
    passports = []
    p = ''
    for line in f.readlines():
        if line.strip() != '': p+=line.strip()+' '
        else:
            passports.append(p)
            p=''
    if p!='': passports.append(p)

#Part 1
valid=0
for p in passports:
    tmp = p.strip().split(' ')
    p_ = []
    for s in tmp:
        p_.extend(s.split(':'))
    if len(p_) == 14 and 'cid' not in p_: 
        valid+=1
    elif len(p_) == 16:
        valid+=1
    else: continue
print(valid)

#Part 2
import re
valid=0
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
for p in passports:
    tmp = p.strip().split(' ')
    pp = {}
    for s in tmp:
        s = s.split(':')
        pp[s[0]] = s[1]
    if len(list(pp.keys()))==8 or (len(list(pp.keys()))==7 and 'cid' not in pp.keys()):
        if len(pp['byr']) != 4 or 1920 > int(pp['byr']) or 2002 < int(pp['byr']):
            continue
        if len(pp['iyr']) != 4 or 2010 > int(pp['iyr']) or 2020 < int(pp['iyr']):
            continue
        if len(pp['eyr']) != 4 or 2020 > int(pp['eyr']) or 2030 < int(pp['eyr']):
            continue
        if pp['hgt'][-2:] == 'cm':
            if int(pp['hgt'][:-2]) < 150 or  int(pp['hgt'][:-2]) > 193: 
                continue
        if pp['hgt'][-2:] == 'in':
            if int(pp['hgt'][:-2]) < 59 or  int(pp['hgt'][:-2]) > 76: 
                continue
        if pp['hgt'][-2:] not in ['cm', 'in']:
            continue
        if not re.search('^#([0-9a-f]){6}', pp['hcl']): 
            continue
        if pp['ecl'] not in ecl: 
            continue
        if not re.search('^([0-9]){9}$', pp['pid']): 
            continue
        valid+=1
print(valid)