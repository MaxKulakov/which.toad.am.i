#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8


# Thanks Joan Stark, Hayley Jane Wakenshaw
# Morfina, Veronica Karlsson, lgbeard
# For Art


import os
import time
import random


def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear')

def out_green(text):
    print("\033[32m {}" .format(text))


def out_text(text):
    print("")
    print(text)
    print("")

def print_toad_1():
    out_green("              _         _")
    out_green("  __   ___.--'_`.     .'_`--.___   __")
    out_green(" ( _`.'. -   'o` )   ( 'o`   - .`.'_ )")
    out_green(" _\.'_'      _.-'     `-._      `_`./_")
    out_green("( \`. )    //\`         '/\\    ( .'/ )")
    out_green(" \_`-'`---'\\__,       ,__//`---'`-'_/")
    out_green("   `                               '  ")
    print("\033[30m {}" .format(""))

def print_toad_2():
    print("")
    out_green("Ты")
    out_green("Мелкая")
    out_green("Жабка")
    print("")
    out_green("  o")
    out_green("_`O'_")
    print("\033[30m {}" .format(""))

def print_toad_3():
    out_green("         Ты")
    out_green("     Подростковая")
    out_green("        Жабка")
    out_green("        ()-()")
    out_green("      .-(___)-.")
    out_green("       _<   >_")
    out_green("       \/   \/")
    print("\033[30m {}" .format(""))

def print_toad_4():
    out_green("Ты натуральная жабка")
    out_green("       _e-e_")
    out_green("     _(-._.-)_")
    out_green("  .-(  `---'  )-.")
    out_green(" __\ \\\___/// /__")
    out_green("'-._.'/M\ /M\`._,-")
    print("\033[30m {}" .format(""))

def print_toad_5():
    out_green("     Ты созревающая жабка")
    out_green("            _     _")
    out_green("           (')-=-(')")
    out_green("         __(   '   )__")
    out_green("        / _/'-----'\_ \ ")
    out_green("     ___\\ \\     // //___")
    out_green("     >____)/_\---/_\(____<")
    print("\033[30m {}" .format(""))

def print_toad_6():
    out_green("  Ты уставшая жабка")
    out_green("        _  _")
    out_green("       (.)(.)")
    out_green("   ,-.(.____.),-.  ")
    out_green("  ( \ \ '--' / / )")
    out_green("   \ \ / ,. \ / /")
    out_green("    ) '| || |' ( ")
    out_green("OoO'- OoO''OoO -'OoO")
    print("\033[30m {}" .format(""))

def print_toad_7():
    out_green("  Ты гоп-стоп жабка")
    out_green("         _ _")
    out_green("        (oTo)")
    out_green("     _.-( _ )-._")
    out_green("    `/`( '-' )`\`")
    out_green("       /'---'\ ")
    out_green("     __\     /__")
    out_green("     \_/     \_/")
    print("\033[30m {}" .format(""))

def print_toad_8():
    out_green("     Ты отбивная жабка")
    out_green("            _   _")
    out_green("           (.)_(.)")
    out_green("        _ (   _   ) _")
    out_green("       / \/`-----'\/ \ ")
    out_green("     __\ ( (     ) ) /__")
    out_green("     )   /\ \._./ /\   (")
    out_green("      )_/ /|\   /|\ \_(")
    print("\033[30m {}" .format(""))

def print_toad_9():
    out_green(" Ты интересная жабка")
    out_green("     /     \ ")
    out_green("     _(I)(I)_")
    out_green("    ( _ .. _ )")
    out_green("     `.`--'.'")
    out_green("      )    (")
    out_green("  ,-./      \,-.")
    out_green(" ( _( ||  || )_ )")
    out_green("__\ \\||--||'/ /__ hjw")
    out_green("`-._//||\/||\\_.-'")
    out_green("     `--'`--'")
    print("\033[30m {}" .format(""))

def print_toad_10():
    out_green("       Ты жирная жабка")
    out_green("           .--._.--.")
    out_green("          ( O     O )")
    out_green("          /   . .   \ ")
    out_green("         .`._______.'.")
    out_green("        /(           )\ ")
    out_green("      _/  \  \   /  /  \_")
    out_green("   .~   `  \  \ /  /  '   ~.")
    out_green("  {    -.   \  V  /   .-    }")
    out_green("_ _`.    \  |  |  |  /    .'_ _")
    out_green(">_       _} |  |  | {_       _<")
    out_green(" /. - ~ ,_-'  .^.  `-_, ~ - .\ ")
    out_green("         '-'|/   \|`-`")
    print("\033[30m {}" .format(""))

def print_toad_11():
    out_green("     Ты жабка на движе")
    out_green("          ,-.___.-.")
    out_green("       ,-.(|)   (|),-.")
    out_green("       \_*._ ' '_.* _/")
    out_green("        /`-.`--' .-'\ ")
    out_green("   ,--./    `---'    \,--.")
    out_green("   \   |(  )     (  )|   /")
    out_green("    \  | ||       || |  /")
    out_green("     \ | /|\     /|\ | /")
    out_green("     /  \-._     _,-/  \ ")
    out_green("    //| \\  `---'  // |\\ ")
    out_green("   /,-.,-.\       /,-.,-.\ ")
    out_green("  o   o   o      o   o    o")
    print("\033[30m {}" .format(""))

def print_toad_12():
    out_green("   Ты королевская жабка")
    out_green("         o  o   o  o")
    out_green("         |\/ \^/ \/|")
    out_green("         |,-------.|")
    out_green("       ,-.(|)   (|),-.")
    out_green("       \_*._ ' '_.* _/")
    out_green("        /`-.`--' .-'\ ")
    out_green("   ,--./    `---'    \,--.")
    out_green("   \   |(  )     (  )|   /")
    out_green("    \  | ||       || |  /")
    out_green("     \ | /|\     /|\ | /")
    out_green("     /  \-._     _,-/  \ ")
    out_green("    //| \\  `---'  // |\\ ")
    out_green("   /,-.,-.\       /,-.,-.\ ")
    out_green("  o   o   o      o   o    o")
    print("\033[30m {}" .format(""))


def print_toad_13():
    out_green("                Ты легендарная магическая жабка")
    out_green("                             .-----.")
    out_green("                            /7  .  (")
    out_green("                           /   .-.  \ ")
    out_green("                          /   /   \  \ ")
    out_green("                         / `  )   (   )")
    out_green("                        / `   )   ).  \ ")
    out_green("                      .'  _.   \_/  . |")
    out_green("     .--.           .' _.' )`.        |")
    out_green("    (    `---...._.'   `---.'_)    ..  \ ")
    out_green("     \            `----....___    `. \  |")
    out_green("      `.           _ ----- _   `._  )/  |")
    out_green("        `.       /'  \   /'  \`.  `._   |")
    out_green("          `.    ((O)` ) ((O)` ) `.   `._\ ")
    out_green("            `-- '`---'   `---' )  `.    `-.")
    out_green("               /                  ` \      `-.")
    out_green("             .'                      `.       `.")
    out_green("            /                     `  ` `.       `-.")
    out_green("     .--.   \ ===._____.======. `    `   `. .___.--`     .''''.")
    out_green("    ' .` `-. `.                )`. `   ` ` \          .' . '  8)")
    out_green("   (8  .  ` `-.`.               ( .  ` `  .`\      .'  '    ' /")
    out_green("    \  `. `    `-.               ) ` .   ` ` \  .'   ' .  '  /")
    out_green("     \ ` `.  ` . \`.    .--.     |  ` ) `   .``/   '  // .  /")
    out_green("      `.  ``. .   \ \   .-- `.  (  ` /_   ` . / ' .  '/   .'")
    out_green("        `. ` \  `  \ \  '-.   `-'  .'  `-.  `   .  .'/  .'")
    out_green("          \ `.`.  ` \ \    ) /`._.`       `.  ` .  .'  /")
    out_green("        |  `.`. . \ \  (.'               `.   .'  .'")
    out_green("        __/  .. \ \ ` ) \                     \.' .. \__")
    out_green(" .-._.-'     ''  / .-'   `.                   \  ''     `-._.--.")
    out_green("(_________.-====' / .' /\_)`--..__________..-- `====-. _________)")
    out_green("                 (.'(.'")
    print("\033[30m {}" .format(""))

def print_toad_14():
    out_green("         Ты влюблённая жабка")
    out_green("              _         _")
    out_green("  __   ___.--'_`.     .'_`--.___   __")
    out_green(" ( _`.'. -   'o` )   ( 'o`   - .`.'_ )")
    out_green(" _\.'_'      _.-'     `-._      `_`./_")
    out_green("( \`. )    //\`         '/\\    ( .'/ )")
    out_green(" \_`-'`---'\\__,       ,__//`---'`-'_/")
    out_green("   `                               '  ")
    print("\033[30m {}" .format(""))


# Main program
clear_term()
out_text("         Какая ты сегодня жабка?       ")
print_toad_1()
# print_toad_12()
time.sleep(2)

symbol = ["               #!5!.#-=04#             ", "               1#!6!4#/=\             "]
def select_text():
    i = 1
    while i <= 15:
        clear_term()
        print("")
        print("               Идёт подбор           ")
        print(symbol[i % 2])
        time.sleep(0.2)
        i += 1
select_text()

clear_term()

num_toad = random.randint(1, 14)
if num_toad == 1:
    print_toad_1()
if num_toad == 2:
    print_toad_2()
if num_toad == 3:
    print_toad_3()
if num_toad == 4:
    print_toad_4()
if num_toad == 5:
    print_toad_5()
if num_toad == 6:
    print_toad_6()
if num_toad == 7:
    print_toad_7()
if num_toad == 8:
    print_toad_8()
if num_toad == 9:
    print_toad_9()
if num_toad == 10:
    print_toad_10()
if num_toad == 11:
    print_toad_11()
if num_toad == 12:
    print_toad_12()
if num_toad == 13:
    print_toad_13()
if num_toad == 14:
    print_toad_14()

print("")
print("")
print("")
time.sleep(2)
