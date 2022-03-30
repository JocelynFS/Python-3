
menu = {
    "1 ": "1. Bisonte",
    "2 ": "2. Pez",
    "3": "3. Zorro",
    "0" : "0. Salir"
}
  
while True:
    print('Muéstrame un animal.')
    for opcion in menu:
        print(menu.get(opcion))
    eleccion = int(input('Elija la opción deseada: '))
    if eleccion == 0:
        break
    elif eleccion == 1:
        print(r"""
             _.-````'-,_
   _,.,_ ,-'`           `'-.,_
 /)     (\                   '``-.
((      ) )                      `\
 \)    (_/                        )\
  |       /)           '    ,'    / \
  `\    ^'            '     (    /  ))
    |      _/\ ,     /    ,,`\   (  "`
     \Y,   |  \  \  | ````| / \_ \
       `)_/    \  \  )    ( >  ( >
                \( \(     |/   |/
               /_(/_(    /_(  /_(
""")
    elif eleccion == 2:
        print(r"""
|\   \\\\__     o
| \_/    o \    o 
> _   (( <_  oo  
| / \__+___/      
|/     |/
""")
    elif eleccion == 3:
        print(r"""
|\_/|,,_____,~~`
(.".)~~     )`~}}
 \o/\ /---~\\ ~}}
   _//    _// ~}
""")
    else:
        print('Opción inválida')



