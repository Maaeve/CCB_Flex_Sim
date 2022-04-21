"""
MAIN SCRIPT VERSION 21/04/2022 15:14
"""
import os
import os.path

import pandas
import numpy as np

#Read CCB configuration input file
NameFile_CCB_Configuration   = 'CCBConfiguration.xlsx'
CCB_DHWConfiguration         = pandas.read_excel(NameFile_CCB_Configuration,sheet_name =  'DHW')  
CCB_SHConfiguration          = pandas.read_excel(NameFile_CCB_Configuration,sheet_name =  'SH')
CCB_BUHConfiguration         = pandas.read_excel(NameFile_CCB_Configuration,sheet_name =  'BUH')
CCB_GeneralConfiguration     = pandas.read_excel(NameFile_CCB_Configuration,sheet_name =  'General')
CCB_WriteDataConfiguration   = pandas.read_excel(NameFile_CCB_Configuration,sheet_name =  'General', dtype=str)
CCB_DHW                      = CCB_DHWConfiguration.iloc[0:10,1].values.tolist()
CCB_SH                       = CCB_SHConfiguration.iloc[0:9,1].values.tolist()
CCB_BUH                      = CCB_BUHConfiguration.iloc[0:5,1].values.tolist()
CCB_General                  = CCB_GeneralConfiguration.iloc[0:3,1].values.tolist()
CCB_WriteData                = CCB_WriteDataConfiguration.iloc[0:4,1]

DHW_service                  = CCB_DHW[0]
COPDHW                       = CCB_DHW[1]
t_DHW_heatup                 = CCB_DHW[2]
T_DHW_ref                    = CCB_DHW[3]
T_DHWmax1                    = CCB_DHW[4]
T_DHWmax2                    = CCB_DHW[5]
V_TES_DHW                    = CCB_DHW[6]/1000
QlossDHW                     = (CCB_DHW[7]*1000/24)/45
E_DHW_Profile_extraction_24h = CCB_DHW[8]
tfactorDHW_reducedday        = (CCB_DHW[9])/(24*60)

Q35rated                     = CCB_SH[0]
V_TES_SH                     = CCB_SH[1]/1000 
T_SHmax1                     = CCB_SH[2]
T_SHmax2                     = CCB_SH[3]
QlossSH                      = (CCB_SH[4]*1000/24)/45
COP35SH_88                   = CCB_SH[5]
COP35SH_54                   = CCB_SH[6]
COP35SH_35                   = CCB_SH[7]
COP35SH_15                   = CCB_SH[8]

BUH_service                  = CCB_BUH[0]
BUH_simultaneous_SH          = CCB_BUH[1]
BUH_simultaneous_DHW         = CCB_BUH[2]
PBUH                         = CCB_BUH[3]
PBUHmin                      = CCB_BUH[4]
Mod_min_BUH                  = PBUHmin/PBUH

timestep                     = CCB_General[0]
casenumber                   = CCB_General[1]
DifferentFolder              = CCB_General[2]
SeparatedFileFolder          = CCB_WriteData[3]
GeneralFileFolder            = cur_dir = os.getcwd()
GeneralFileFolder            = GeneralFileFolder+"\\"

if DifferentFolder==0:
    FileFolder=GeneralFileFolder
elif DifferentFolder==1:
    FileFolder=SeparatedFileFolder
else:
    FileFolder=GeneralFileFolder
    print("An error in the determination of a separated folder for storing the result files occured.")
    print("Please make sure that only the values 0 (Main Python Folder) or 1 (Specify specific directory via the variable 'filelocation') are valid.")
    print("Due to the error, your result files are stored in your main Python folder")
FileLocDetailed              = FileFolder+"Case"+str(casenumber)+"_"
FileLocFinal                 = FileFolder+"Case"+str(casenumber)+"_Result.txt"

#Read heat pump data input file
NameFile_HP_Data = 'PerformanceData.xlsx'
HP_88              = pandas.read_excel(NameFile_HP_Data,sheet_name =  'HP_Data_-7°C')     
HP_54              = pandas.read_excel(NameFile_HP_Data,sheet_name =  'HP_Data_12°C')   
HP_35              = pandas.read_excel(NameFile_HP_Data,sheet_name =  'HP_Data_7°C') 
HP_15              = pandas.read_excel(NameFile_HP_Data,sheet_name =  'HP_Data_2°C')     
HP_Modulations     = pandas.read_excel(NameFile_HP_Data,sheet_name =  'HP_Data_Modulation')              

Q_HP_88            =  HP_88.iloc[0:7,1].values.tolist()
Q_HP_54            =  HP_54.iloc[0:7,1].values.tolist()
Q_HP_35            =  HP_35.iloc[0:7,1].values.tolist()
Q_HP_15            =  HP_15.iloc[0:7,1].values.tolist()
P_HP_88            =  HP_88.iloc[7:14,1].values.tolist()
P_HP_54            =  HP_54.iloc[7:14,1].values.tolist()
P_HP_35            =  HP_35.iloc[7:14,1].values.tolist()
P_HP_15            =  HP_15.iloc[7:14,1].values.tolist()
P_HP_15            =  HP_15.iloc[7:14,1].values.tolist()
HP_Mods            =  HP_Modulations.iloc[0:8,1].values.tolist()

Q30_55_88  = Q_HP_88[0]
Q50_55_88  = Q_HP_88[1]
Q70_55_88  = Q_HP_88[2]
Q90_55_88  = Q_HP_88[3]
Q100_55_88 = Q_HP_88[4]
Q100_45_88 = Q_HP_88[5]
Q100_35_88 = Q_HP_88[6]
P30_55_88  = P_HP_88[0]
P50_55_88  = P_HP_88[1]
P70_55_88  = P_HP_88[2]
P90_55_88  = P_HP_88[3]
P100_55_88 = P_HP_88[4]
P100_45_88 = P_HP_88[5]
P100_35_88 = P_HP_88[6]
    
Q30_55_54  = Q_HP_54[0]
Q50_55_54  = Q_HP_54[1]
Q70_55_54  = Q_HP_54[2]
Q90_55_54  = Q_HP_54[3]
Q100_55_54 = Q_HP_54[4]
Q100_45_54 = Q_HP_54[5]
Q100_35_54 = Q_HP_54[6]
P30_55_54  = P_HP_54[0]
P50_55_54  = P_HP_54[1]
P70_55_54  = P_HP_54[2]
P90_55_54  = P_HP_54[3]
P100_55_54 = P_HP_54[4]
P100_45_54 = P_HP_54[5]
P100_35_54 = P_HP_54[6]

Q30_55_35  = Q_HP_35[0]
Q50_55_35  = Q_HP_35[1]
Q70_55_35  = Q_HP_35[2]
Q90_55_35  = Q_HP_35[3]
Q100_55_35 = Q_HP_35[4]
Q100_45_35 = Q_HP_35[5]
Q100_35_35 = Q_HP_35[6]
P30_55_35  = P_HP_35[0]
P50_55_35  = P_HP_35[1]
P70_55_35  = P_HP_35[2]
P90_55_35  = P_HP_35[3]
P100_55_35 = P_HP_35[4]
P100_45_35 = P_HP_35[5]
P100_35_35 = P_HP_35[6]

Q30_55_15  = Q_HP_15[0]
Q50_55_15  = Q_HP_15[1]
Q70_55_15  = Q_HP_15[2]
Q90_55_15  = Q_HP_15[3]
Q100_55_15 = Q_HP_15[4]
Q100_45_15 = Q_HP_15[5]
Q100_35_15 = Q_HP_15[6]
P30_55_15  = P_HP_15[0]
P50_55_15  = P_HP_15[1]
P70_55_15  = P_HP_15[2]
P90_55_15  = P_HP_15[3]
P100_55_15 = P_HP_15[4]
P100_45_15 = P_HP_15[5]
P100_35_15 = P_HP_15[6]  

Mod_level5       = HP_Mods[0]/100
Mod_level4        = HP_Mods[1]/100
Mod_level3        = HP_Mods[2]/100
Mod_level2        = HP_Mods[3]/100
Mod_level1        = HP_Mods[4]/100
Mod_min_Comp = Mod_level1
Tcomp1      = HP_Mods[5]
Tcomp2      = HP_Mods[6]
Tcomp3      = HP_Mods[7]

#CaseType==1000 refers to an undefined case
#CaseType==1001 indicates that the constraint of Tcomp3 = T_SHmax1 = T_DHWmax1 was not met
#CaseType==1002 indicates that the constraints of (Tcomp1 <= 35 °C) < Tcomp2 < Tcomp3 and/or Mod_level1 < Mod_level2 < Mod_level3 < Mod_level4 < Mod_level5 were not met

if DHW_service==0:
    if BUH_service==0:
        CaseType=1
    elif BUH_service==1:
        CaseType=0
    else:
        CaseType=1000
elif DHW_service==1:
    if BUH_service==0:
        CaseType=2
    elif BUH_service==1:
        if BUH_simultaneous_SH==1:
            if BUH_simultaneous_DHW==0:
                CaseType=3
            elif BUH_simultaneous_DHW==1:
                CaseType=0
            else:
                CaseType=1000
        elif BUH_simultaneous_SH==0:
            if BUH_simultaneous_DHW==0:
                CaseType=4
            elif BUH_simultaneous_DHW==1:
                CaseType=0
            else:
                CaseType=1000            
        else:
            CaseType=1000
    else:
        CaseType=1000
else:
    CaseType=1000    

if Tcomp3!=T_SHmax1 or Tcomp3!=T_DHWmax1:
    CaseType=1001 

if (Tcomp1 < Tcomp2 < Tcomp3) and (Tcomp1 <= 35) and (Mod_level1 < Mod_level2 < Mod_level3 < Mod_level4 < Mod_level5):
    CaseType=CaseType
else:
    CaseType=1002
    
if CaseType==1:
    from Cases_1_4_subscripts import *    
    main_cases_1_4(Q35rated,COP35SH_88,COP35SH_54,COP35SH_35,COP35SH_15,V_TES_SH,QlossSH,
                   Q30_55_88,Q50_55_88,Q70_55_88,Q90_55_88,Q100_55_88,Q100_45_88,Q100_35_88,P30_55_88,P50_55_88,P70_55_88,P90_55_88,P100_55_88,P100_45_88,P100_35_88,
                   Q30_55_54,Q50_55_54,Q70_55_54,Q90_55_54,Q100_55_54,Q100_45_54,Q100_35_54,P30_55_54,P50_55_54,P70_55_54,P90_55_54,P100_55_54,P100_45_54,P100_35_54,
                   Q30_55_35,Q50_55_35,Q70_55_35,Q90_55_35,Q100_55_35,Q100_45_35,Q100_35_35,P30_55_35,P50_55_35,P70_55_35,P90_55_35,P100_55_35,P100_45_35,P100_35_35,
                   Q30_55_15,Q50_55_15,Q70_55_15,Q90_55_15,Q100_55_15,Q100_45_15,Q100_35_15,P30_55_15,P50_55_15,P70_55_15,P90_55_15,P100_55_15,P100_45_15,P100_35_15,
                   Mod_level5,Mod_level4,Mod_level3,Mod_level2,Mod_level1,Mod_min_Comp,timestep,FileLocDetailed,FileLocFinal,T_SHmax1,Tcomp1,Tcomp2,Tcomp3)
elif CaseType==2:
    from Cases_5_8_subscripts import *
    main_cases_5_8(Q35rated,COP35SH_88,COP35SH_54,COP35SH_35,COP35SH_15,V_TES_SH,QlossSH,
                   Q30_55_88,Q50_55_88,Q70_55_88,Q90_55_88,Q100_55_88,Q100_45_88,Q100_35_88,P30_55_88,P50_55_88,P70_55_88,P90_55_88,P100_55_88,P100_45_88,P100_35_88,
                   Q30_55_54,Q50_55_54,Q70_55_54,Q90_55_54,Q100_55_54,Q100_45_54,Q100_35_54,P30_55_54,P50_55_54,P70_55_54,P90_55_54,P100_55_54,P100_45_54,P100_35_54,
                   Q30_55_35,Q50_55_35,Q70_55_35,Q90_55_35,Q100_55_35,Q100_45_35,Q100_35_35,P30_55_35,P50_55_35,P70_55_35,P90_55_35,P100_55_35,P100_45_35,P100_35_35,
                   Q30_55_15,Q50_55_15,Q70_55_15,Q90_55_15,Q100_55_15,Q100_45_15,Q100_35_15,P30_55_15,P50_55_15,P70_55_15,P90_55_15,P100_55_15,P100_45_15,P100_35_15,
                   Mod_level5,Mod_level4,Mod_level3,Mod_level2,Mod_level1,Mod_min_Comp,timestep,FileLocDetailed,FileLocFinal,COPDHW,t_DHW_heatup,T_DHW_ref,V_TES_DHW,QlossDHW,
                   E_DHW_Profile_extraction_24h,tfactorDHW_reducedday,T_SHmax1,T_DHWmax1,Tcomp1,Tcomp2,Tcomp3)
elif CaseType==3:
    from Cases_9_12_subscripts import *
    main_cases_9_12(Q35rated,COP35SH_88,COP35SH_54,COP35SH_35,COP35SH_15,V_TES_SH,QlossSH,
                   Q30_55_88,Q50_55_88,Q70_55_88,Q90_55_88,Q100_55_88,Q100_45_88,Q100_35_88,P30_55_88,P50_55_88,P70_55_88,P90_55_88,P100_55_88,P100_45_88,P100_35_88,
                   Q30_55_54,Q50_55_54,Q70_55_54,Q90_55_54,Q100_55_54,Q100_45_54,Q100_35_54,P30_55_54,P50_55_54,P70_55_54,P90_55_54,P100_55_54,P100_45_54,P100_35_54,
                   Q30_55_35,Q50_55_35,Q70_55_35,Q90_55_35,Q100_55_35,Q100_45_35,Q100_35_35,P30_55_35,P50_55_35,P70_55_35,P90_55_35,P100_55_35,P100_45_35,P100_35_35,
                   Q30_55_15,Q50_55_15,Q70_55_15,Q90_55_15,Q100_55_15,Q100_45_15,Q100_35_15,P30_55_15,P50_55_15,P70_55_15,P90_55_15,P100_55_15,P100_45_15,P100_35_15,
                   Mod_level5,Mod_level4,Mod_level3,Mod_level2,Mod_level1,Mod_min_Comp,timestep,FileLocDetailed,FileLocFinal,COPDHW,t_DHW_heatup,T_DHW_ref,V_TES_DHW,QlossDHW,
                   E_DHW_Profile_extraction_24h,tfactorDHW_reducedday,T_SHmax1,T_DHWmax1,T_SHmax2,T_DHWmax2,PBUH,Mod_min_BUH,Tcomp1,Tcomp2,Tcomp3)
elif CaseType==4:
    from Cases_13_16_subscripts import *
    main_cases_13_16(Q35rated,COP35SH_88,COP35SH_54,COP35SH_35,COP35SH_15,V_TES_SH,QlossSH,
                   Q30_55_88,Q50_55_88,Q70_55_88,Q90_55_88,Q100_55_88,Q100_45_88,Q100_35_88,P30_55_88,P50_55_88,P70_55_88,P90_55_88,P100_55_88,P100_45_88,P100_35_88,
                   Q30_55_54,Q50_55_54,Q70_55_54,Q90_55_54,Q100_55_54,Q100_45_54,Q100_35_54,P30_55_54,P50_55_54,P70_55_54,P90_55_54,P100_55_54,P100_45_54,P100_35_54,
                   Q30_55_35,Q50_55_35,Q70_55_35,Q90_55_35,Q100_55_35,Q100_45_35,Q100_35_35,P30_55_35,P50_55_35,P70_55_35,P90_55_35,P100_55_35,P100_45_35,P100_35_35,
                   Q30_55_15,Q50_55_15,Q70_55_15,Q90_55_15,Q100_55_15,Q100_45_15,Q100_35_15,P30_55_15,P50_55_15,P70_55_15,P90_55_15,P100_55_15,P100_45_15,P100_35_15,
                   Mod_level5,Mod_level4,Mod_level3,Mod_level2,Mod_level1,Mod_min_Comp,timestep,FileLocDetailed,FileLocFinal,COPDHW,t_DHW_heatup,T_DHW_ref,V_TES_DHW,QlossDHW,
                   E_DHW_Profile_extraction_24h,tfactorDHW_reducedday,T_SHmax1,T_DHWmax1,T_SHmax2,T_DHWmax2,PBUH,Mod_min_BUH,Tcomp1,Tcomp2,Tcomp3)
elif CaseType==0:
    print("We are sorry to tell you that your specific case could not be placed within the available cases.")
    print("Please take contact with the code developers, so that they can help to include your case as well.")
elif CaseType==1001:
    print("Please make sure that the maximum compressor supply temperature Tcomp3 equals both TSH_max1 and TDHW_max1.")
    print("Tcomp3 = T_SHmax1 = T_DHWmax1")
    print("Tcomp3 can be found in 'PerformanceData.xlsx' under the tab 'HP_Data_Modulation'.")
    print("T_SHmax1 can be found in 'CCBConfiguration.xlsx' under the tab 'SH'.")
    print("T_DHWmax1 can be found in 'CCBConfiguration.xlsx' under the tab 'DHW'.")
elif CaseType==1002:
    print("Please make sure that the following constraints in the file 'PerformanceData.xlsx' are met: ")
    print("(Tcomp1 <= 35 °C) < Tcomp2 < Tcomp3")
    print("Mod_level1 < Mod_level2 < Mod_level3 < Mod_level4 < Mod_level5")
    
else:
    print("An invalid number for DHW_service, BUH_service, BUH_simultaneous_SH, BUH_simultaneous_DHW, BUH_separated_SH or BUH_separated_DHW was entered.")
    print("Please make sure that the aforementioned control variables are only 0 (service not include) or 1 (service included).")
    print("Please make sure that when BUH_service is active, that only one of the two options (simultaneous or separated operation) within one heat service (SH or DHW) is used.")  