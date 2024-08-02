import csv

f = open('Leader-Follower_result_Query-1.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
   data.append(row)
f.close()

# print(data[1:])

def convert_row(row):
    return """<Price_Map_Set>
<Price_Map_Record>
<Component_Type_Name>%s</Component_Type_Name>
<From_Domain>%s</From_Domain>
<From_Dimension_Set>%s</From_Dimension_Set>
<From_Dimension_Value>%s</From_Dimension_Value>
<To_Domain>%s</To_Domain>
<To_Dimension_Set>%s</To_Dimension_Set>
<To_Dimension_Value>%s</To_Dimension_Value>
<Map_Group_Name>%s</Map_Group_Name>
<Map_Type>%s</Map_Type>
<Extraction_Time>%s</Extraction_Time>
</Price_Map_Record>
</Price_Map_Set>
""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

with open('BP.PRICEMAP.xml', "w") as f:
    f.write('\n'.join([convert_row(row) for row in data]))