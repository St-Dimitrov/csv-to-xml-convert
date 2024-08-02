import csv

# select the files name in the open() function
f = open('Leader-Follower_Result-Query-2.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
   data.append(row)
f.close()

# print(data[1:])
#EDIT the number and names of the row names to match your desired xml output --- no need to change the value
def convert_row(row):
    return """<Leader_Follower_Rule_Set>
<Leader_Follower_Rule_Record>
<Component_Type_Upload_Code>%s</Component_Type_Upload_Code>
<Price_Level_Upload_Code>%s</Price_Level_Upload_Code>
<Dimension_Set>%s</Dimension_Set>
<Leader_Scope>%s</Leader_Scope>
<Follower_Scope>%s</Follower_Scope>
<Mapping_Mode>%s</Mapping_Mode>
<Mapping_Value>%s</Mapping_Value>
<Extraction_Time>%s</Extraction_Time>
</Leader_Follower_Rule_Record>
</Leader_Follower_Rule_Set>
""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
# number of row[number] must match the number of %s counting from zero

with open('BP.LEADERFOLLOWERRULE.xml', "w") as f:
    f.write('\n'.join([convert_row(row) for row in data]))