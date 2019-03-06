# group, groups,  groupdict
Ref: https://www.hackerrank.com/challenges/re-group-groups/problem
```
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
m.groups
m.group(1,2,3) 
('username', 'hackerrank', 'com')
```
```
>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
```

## hackerrank problem
Q: Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

```
Sample Input
..12345678910111213141516171820212223
Sample Output
1
Explanation
.. is the first repeating character, but it is not alphanumeric. 
1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.
```

**Solution**
```
S = "..12345678910111213141516171820212223"
import re
r=re.search(r'([0-9a-zA-Z])\1',S)
print(r.group(1) if r else -1)
```

## multiline regex example
```
string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
^(?P<last_name>[\w ]*),\s
(?P<first_name>[\w ]*):\s
(?P<score>[\d]*)$
''',string, re.X|re.M)

for player in string.split('\n'):
    print(players.groupdict())
```
