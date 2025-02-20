import xlwings as xw

# # Erstellt eine Excel- Datei und speichert sie
# # wb = xw.Book()
# # wb.save('test.xlsx')

# # Öffnet eine Excel- DAtei zur Bearbeitung
# wb = xw.Book('test.xlsx')

# sheet1 = wb.sheets[0]
# print(sheet1.range('A1').value)
# print(sheet1.cells(1,'A').value)
# sheet1.range('A1').value = 200
# sheet1.range('A1').options(transpose=True).value = [[100,200,300],[400,500,600],[700,800,900]]
# print(sheet1.range('A1').expand().value)
# wb.save()

wb1 = xw.Book('destatis.xlsx')
sheet2 = wb1.sheets['2.5']
#print(sheet2.range('A15').expand().value)
print(sheet2.range('A5:K8').value)