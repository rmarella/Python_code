import cx_Oracle
import sys
import weakref
import traceback
import pyodbc

class XlsFileData:
     
     def __init__(self,str_FilePath):
          #self.connect_XLS=None
          self.str_FilePath=str_FilePath
          self.strConn= (r'DRIVER={Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)};'r'DBQ='+self.str_FilePath+';'r'HDR=YES;'r'ReadOnly=0')
     def __del__(self):
           print "destructor called" 
     #   def getDatabycloumn(str_CloumnName):
     
     def connectxlsFile(self):
          
          connect_XLS = pyodbc.connect(self.strConn,autocommit=True)
          return connect_XLS
          
     connect_XLS=None               
     def getdataByCloumnName(self):
          try:
               
               
               curs1_XLS=self.connectxlsFile().cursor()
               
               excel_results = curs1_XLS.execute(r'select ravi from [Sheet1$]').fetchall()               
               print(excel_results[0][0])
          except:  
                print "Error :"+str(traceback.format_exc())
                
                connect_XLS=None

          finally :    
               connect_XLS=None         
               print ("connect_DB Closed")


Objtemp =XlsFileData("C:\Users\kogentix\Desktop\Python\Test.xlsx")
Objtemp.getdataByCloumnName()
Objtemp=None
