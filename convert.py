# -*- coding: cp1252 -*-
import xlrd
import json
import unicodedata

workbook = xlrd.open_workbook('ambiental.xlsx', encoding_override="cp1252")

s = workbook.sheet_by_index(1)

sala = 'NO SALA'

lista = []

dia = ''


keys = ['fake', 'sem','dis','prof','curso','codTurma','dia', 'hInicio', 'hFim', 'lab', 'comp', 'sala',]

turma = {
  'fake': '',
  'sem': '',
  'dis': '',
  'prof': '',
  'curso': '',
  'codTurma': '',
  'dia': '',
  'hInicio': '',
  'hFim': '',
  'lab': '',
  'comp': '', 
  'sala': '',
}

for i in range(6, 55):
  lista.append(turma)
  turma = {
    'fake': '',
    'sem': '',
    'dis': '',
    'prof': '',
    'curso': '',
    'codTurma': '',
    'dia': '',
    'hInicio': '',
    'hFim': '',
    'lab': '',
    'comp': '', 
    'sala': '',
  }

  dia = ''
  for j in range(1, 11):
    if type(s.cell(i, j).value) == float:
      turma[keys[j]] = s.cell(i, j).value
      print 'aqui'
    elif (j == 11) and (i > 6):
      if s.cell(i, j).value == '':
        turma[keys[j]] = sala
      elif s.cell(i, j).value == 'Sala':
        print('X')
      else:
        sala = s.cell(i, j).value
        turma[keys[j]] = sala
    elif s.cell(i, j).value == '':
      print('X')     
    elif s.cell(i, j).value == 'Sem':
      print('X')    
    elif s.cell(i, j).value == 'Disciplinas':
      print('X')
    elif s.cell(i, j).value == 'Disciplinas':
      print('X')
    elif s.cell(i, j).value == 'Professor':
      print('X')
    elif s.cell(i, j).value == 'Curso':
      print('X')
    elif unicodedata.normalize('NFKD', s.cell(i, j).value).encode('ASCII', 'ignore') == 'Codigo':
      print('X')
    elif s.cell(i, j).value == 'Dia':
      print('X')
    elif unicodedata.normalize('NFKD', s.cell(i, j).value).encode('ASCII', 'ignore') == 'Horario Inicial':
      print('X')
    elif unicodedata.normalize('NFKD', s.cell(i, j).value).encode('ASCII', 'ignore') == 'Horario Final':
      print('X')
    elif s.cell(i, j).value == 'Lab.':
      print('X')
    elif s.cell(i, j).value == 'Compartilhada':
      print('X')
    elif s.cell(i, j).value == 'Sala':
      print('X')
    else:
      turma[keys[j]] = s.cell(i, j).value



print(json.dumps(lista))