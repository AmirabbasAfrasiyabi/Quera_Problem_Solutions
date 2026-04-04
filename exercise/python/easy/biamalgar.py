a,b,c=map(int,input().split('?'))
r=-10**100
for x in'+*':
 for y in'+*':
  r=max(r,eval(f'({a}{x}{b}){y}{c}'),eval(f'{a}{x}({b}{y}{c})'))
print(r)