#Ask for a name
name = input('Enter a name: ')
#A color
color= input('Enter a color: ')
#An insult
insult = input('Enter an insult: ')

f = open(f'{name}.html','w')
html_template = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style='background-color:{color}'>
    <h2>{name}</h2>
    <p>Sidy is {insult}</p>
</body>
</html>
"""
f.write(html_template)

f.close()