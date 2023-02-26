#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  PyCheck.py
#  
#  Copyright 2023 Sebastian Nestler
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import PySimpleGUI as sg

sg.theme('LightBlue2')

layout = [
          [sg.Text('Enter the original Hash here:'), sg.Text(size=(64,1), key='Hash1')],
          [sg.Input(key='#1')],
          [sg.Text('Enter the calculated Hash below: '), sg.Text(size=(64,1), key='Hash2')],
          [sg.Input(key='#2')],
          [sg.Button('Compare')], 
          [sg.Text(size=(64,1), key='-OUTPUT-')],
          [sg.Button('Exit')]
         ]

window = sg.Window('PyCheck', layout)
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Compare':
        if values['#1'] == '' or values['#2'] == '':
            window['-OUTPUT-'].update('Please enter both hashes.')
        elif values['#1'] == values['#2']:
            window['-OUTPUT-'].update('The hashes are equal.')
        else:
            window['-OUTPUT-'].update('Cave! Hashes are not equal. The file may have been manipulated!')
    
window.close()





