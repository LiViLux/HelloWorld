import sys
import mysql.connector
from mysql.connector import errorcode
from distutils.sysconfig import get_python_lib

print("\npython_lib")
print(get_python_lib())

print("\nsys.version")
print(sys.version)

print("\nHello World\nMy name is GI\n")

# print multiple lines
print("""
Usage: HelloWorld [OPTIONS]
   -g      Send hello to G
   -i      Send hello to I
""")

# Test DB connectivity
try:
    cnx = mysql.connector.connect(user='lividatadb1',
                                  database='lividatadb1',
                                  password='dojaja',
                                  host='192.168.150.136')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

# Open database connection
cnx = mysql.connector.connect(user='lividatadb1',
                              database='lividatadb1',
                              password='dojaja',
                              host='192.168.150.136')

# prepare a cursor object using cursor() method
cursor = cnx.cursor()

# define sql query
sql = "SELECT * FROM Table1 ORDER BY 1 ASC"

# Execute the SQL command
cursor.execute(sql)

# Fetch all the rows, cout of rows and colum names wit cursor
results = cursor.fetchall()
results_rowcount = cursor.rowcount
results_column_names = cursor.column_names

# Now print fetched data
print("\nColum Names:    ", results_column_names)
print("\nNr of records  :", results_rowcount)
print("\nFetchAll:  ", results)
results.reverse()
print("\nReversed:  ", results)
print("\nMax:  ", max(results))
print("\nMin:  ", min(results))
print("\n2nd and 3rd row:   ", results[1:3])
print("\nFirst row:\n", results[0:1])
print("\nFirst row:  ", results[0])

# use INPUT for user input and to select and display row as a list and then as string
member_nr = input("\nPlease enter Member Nr: ")
cursor = cnx.cursor()
sql2 = ("SELECT * FROM Table1 WHERE Column1 = " + member_nr)
cursor.execute(sql2)
results2 = cursor.fetchone()  # fecth one complet DB row with cursor, store it in result2 list

# disconnect from DB server
cnx.close()

print("DB record for: ", member_nr, " is\n", results2)  # print whole list
print(results2[0])  # print first column from fetched DB row ie list
print(results2[1])  # print second column from fetched DB row ie list
#print(results2[2])  # print third column from fetch DB row ie list

member_nr_from_list = results2[0]
member_name_from_list = results2[1]
#member_age_from_list = results2[2]
print("\nNoFromList:    ", member_nr_from_list)
print("\nNameFromList:  ", member_name_from_list)
#print("\nAgeFromList:   ", member_age_from_list)

# convert to string and split the string into 3 new strings
mymember = ' '.join(map(str, results2))
print("\nString:  ", mymember)
#member_nr, member_name, member_age = mymember.split()
member_nr, member_name = mymember.split()
print("\nNo:    ", member_nr)
print("\nName:  ", member_name)
#print("\nAge:   ", member_age)

# use db rowcount to loop thru result list
countup = results_rowcount - 1
while countup >= 0:
    print("\nRecord No: ", countup, "od ", results_rowcount - 1, "recorda totalno", end=";")
    print("\nPokazi Record No ", countup, " iz Rezults: ", results[countup:(countup + 1)])
    countup = countup - 1

x = int(input("\nPlease enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")