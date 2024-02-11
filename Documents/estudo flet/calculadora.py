import flet as ft
from flet import colors



botoes = [

    {'operador': 'C', 'fonte':colors.ORANGE,'fundo' : colors.GREY_900 },
    {'operador': '()', 'fonte':colors.GREEN,'fundo' : colors.GREY_900},
    {'operador': '%', 'fonte':colors.GREEN,'fundo' : colors.GREY_900 },
    {'operador': '/', 'fonte':colors.GREEN,'fundo' : colors.GREY_900 },
    {'operador': '7', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '8', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '9', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '*', 'fonte':colors.GREEN,'fundo' : colors.GREY_900 },
    {'operador': '4', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '5', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '6', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '-', 'fonte':colors.GREEN,'fundo' : colors.GREY_900 },
    {'operador': '1', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '2', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '3', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '+', 'fonte':colors.GREEN,'fundo' : colors.GREY_900 },
    {'operador': '±', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '0', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '.', 'fonte':colors.WHITE,'fundo' : colors.GREY_900 },
    {'operador': '=', 'fonte':colors.WHITE,'fundo' : colors.GREEN },


]

def menu(page: ft.Page):

    page.bgcolor = '#000000'
    page.window_resizable = False
    page.window_width = 280
    page.window_height = 400
    page.title = 'Calculadora'
    page.window_always_on_top = True


    resultado = ft.Text(value = '0' , color = colors.WHITE , size= 20)

    def calculo(operador, value_atual):
        try:
            value = eval(value_atual)
    
            if operador == '%':
                value /= 100
            elif operador == '±':
                value = -value
            else:
                 return value
        except:
             return 'Error'
            

    def sel(e):
        value_atual = resultado.value if resultado.value not in ('0','ERROR' )else ''
        value = e.control.content.value

        if value.isdigit():
                value = value_atual + value   
        elif value == 'C':
                value = '0'
        else:
            if value_atual and value_atual[-1] in ('/','*','-','.','+'):
                value_atual = value_atual[:-1]
            
            value = value_atual + value

            if value[-1] in ('=','%','±'):
                value = calculo(operador=value[-1], value_atual=value_atual)
            
        resultado.value = value
        resultado.update()

    display = ft.Row(
        width = 350,
        controls = [resultado],
        alignment= 'end' 
    )

    btn = [ft.Container(
         content= ft.Text(value = btn['operador'], color = btn['fonte']),
         width = 50,
         height = 50,
         bgcolor = btn['fundo'] ,
         border_radius = 100,
         alignment = ft.alignment.center,
         on_click=sel
        )for btn in botoes]
    

    teclado = ft.Row(

        width = 350,
        wrap = True,
        controls = btn,
        alignment = 'end' 
    )
    
    page.add(display, teclado)




ft.app(target = menu)