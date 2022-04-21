"""
-------------------------------------------------------------------------------
FUNCTIONS VERSION 21/04/2022 15:14
-------------------------------------------------------------------------------
"""
nseg=10
def main_cases_1_4(Q35rated,COP35SH_88,COP35SH_54,COP35SH_35,COP35SH_15,V_TES_SH,QlossSH,
                   Q30_55_88,Q50_55_88,Q70_55_88,Q90_55_88,Q100_55_88,Q100_45_88,Q100_35_88,P30_55_88,P50_55_88,P70_55_88,P90_55_88,P100_55_88,P100_45_88,P100_35_88,
                   Q30_55_54,Q50_55_54,Q70_55_54,Q90_55_54,Q100_55_54,Q100_45_54,Q100_35_54,P30_55_54,P50_55_54,P70_55_54,P90_55_54,P100_55_54,P100_45_54,P100_35_54,
                   Q30_55_35,Q50_55_35,Q70_55_35,Q90_55_35,Q100_55_35,Q100_45_35,Q100_35_35,P30_55_35,P50_55_35,P70_55_35,P90_55_35,P100_55_35,P100_45_35,P100_35_35,
                   Q30_55_15,Q50_55_15,Q70_55_15,Q90_55_15,Q100_55_15,Q100_45_15,Q100_35_15,P30_55_15,P50_55_15,P70_55_15,P90_55_15,P100_55_15,P100_45_15,P100_35_15,
                   Mod100,Mod90,Mod70,Mod50,Mod30,Mod_min_Comp,timestep,ResultFileDetailed,ResultFileFinal,T_SHmax1,T35,T45,T55):
    #Assumptions:
    # - T55,P55,Q55 is also the final temperature that the compressor will reach.
    #   Therefore, adapt all 5°C powers and temperatures if the compressor should stop earlier or later.
    # - Only 3 tempperature levels are foreseen and only 5 modulation levels.
    #   The provided data can be adapted according the manufacturer data, but the number of levels should be kept
    
    #Thermal space heating power CCB at Toutdoor temperatures for -7°C, 2°C, 7°C and 12°C respectively
    Q35SH_88=((-7-16)/(-10-16))*Q35rated
    Q35SH_54=((2-16)/(-10-16))*Q35rated
    Q35SH_35=((7-16)/(-10-16))*Q35rated
    Q35SH_15=((12-16)/(-10-16))*Q35rated
    
    #Average COP over four outdoor temperature levels at -7°C, 2°C, 7°C and 12°C
    COP35SH_ref=(COP35SH_88+COP35SH_54+COP35SH_35+COP35SH_15)/4
    
    #Room in which the TES is located
    T_env=20
    
    #Minimum/maximum temperatures for SH & DHW according the 2 flexibility cycles
    T_SHmin=35
    
    #Temperature difference for SH and DHW in design conditions
    dT_SHflow=5
    
    #Water density in kg/m³ and heat capacity in J/kg.K at 40°C
    rho=992.22
    cp=4179.6
    
    #CALCULATIONS OF GENERAL DATA FOR CHARGING CYCLE
    #Calculation of mass flow rates in kg/s in design conditions for SH and DHW
    m_SH=Q35rated/(dT_SHflow*cp)
    
    filelocation=ResultFileDetailed
    resultfile=ResultFileFinal

    for i in range(4):
        if i==0:
            Q30_55=Q30_55_88
            Q50_55=Q50_55_88
            Q70_55=Q70_55_88
            Q90_55=Q90_55_88
            Q100_55=Q100_55_88
            Q100_45=Q100_45_88
            Q100_35=Q100_35_88
            P30_55=P30_55_88
            P50_55=P50_55_88
            P70_55=P70_55_88
            P90_55=P90_55_88
            P100_55=P100_55_88
            P100_45=P100_45_88
            P100_35=P100_35_88
            print("DHW AT -7°C")
            print("NOT IN USE")
            case="_DHW_88.txt"  
            t_Charge_DHW8840flex1=0
            Pelec_Charge_DHW8840flex1=0
            T_TES_DHW88_flex1=0
            t_Charge_DHW8840flex2=0
            Pelec_Charge_DHW8840flex2=0
            T_TES_DHW88_flex2=0
            print("SH AT -7°C")
            case="_SH_88.txt"
            t_Charge_SH88flex1,Pelec_Charge_SH88flex1,T_TES_SH88_flex1=charge_no_BUH(filelocation,case,1,Mod100,Mod90,Mod70,Mod50,Mod30,T35,T45,T55,V_TES_SH,QlossSH,m_SH,T_env,rho,cp,T_SHmin,T_SHmax1,timestep,Q30_55,Q50_55,Q70_55,Q90_55,Q100_55,Q100_45,Q100_35,P30_55,P50_55,P70_55,P90_55,P100_55,P100_45,P100_35,Mod_min_Comp)
            t_Charge_SH88flex2=t_Charge_SH88flex1
            Pelec_Charge_SH88flex2=Pelec_Charge_SH88flex1
            T_TES_SH88_flex2=T_TES_SH88_flex1
            print("")
            
        elif i==1:
            Q30_55=Q30_55_54
            Q50_55=Q50_55_54
            Q70_55=Q70_55_54
            Q90_55=Q90_55_54
            Q100_55=Q100_55_54
            Q100_45=Q100_45_54
            Q100_35=Q100_35_54
            P30_55=P30_55_54
            P50_55=P50_55_54
            P70_55=P70_55_54
            P90_55=P90_55_54
            P100_55=P100_55_54
            P100_45=P100_45_54
            P100_35=P100_35_54
            print("DHW AT 2°C")
            print("NOT IN USE")
            case="_DHW_54.txt"
            t_Charge_DHW5440flex1=0
            Pelec_Charge_DHW5440flex1=0
            T_TES_DHW54_flex1=0
            t_Charge_DHW5440flex2=0
            Pelec_Charge_DHW5440flex2=0
            T_TES_DHW54_flex2=0
            print("SH AT 2°C")
            case="_SH_54.txt"
            t_Charge_SH54flex1,Pelec_Charge_SH54flex1,T_TES_SH54_flex1=charge_no_BUH(filelocation,case,1,Mod100,Mod90,Mod70,Mod50,Mod30,T35,T45,T55,V_TES_SH,QlossSH,m_SH,T_env,rho,cp,T_SHmin,T_SHmax1,timestep,Q30_55,Q50_55,Q70_55,Q90_55,Q100_55,Q100_45,Q100_35,P30_55,P50_55,P70_55,P90_55,P100_55,P100_45,P100_35,Mod_min_Comp)
            t_Charge_SH54flex2=t_Charge_SH54flex1
            Pelec_Charge_SH54flex2=Pelec_Charge_SH54flex1
            T_TES_SH54_flex2=T_TES_SH54_flex1
            print("")
            
        elif i==2:
            Q30_55=Q30_55_35
            Q50_55=Q50_55_35
            Q70_55=Q70_55_35
            Q90_55=Q90_55_35
            Q100_55=Q100_55_35
            Q100_45=Q100_45_35
            Q100_35=Q100_35_35
            P30_55=P30_55_35
            P50_55=P50_55_35
            P70_55=P70_55_35
            P90_55=P90_55_35
            P100_55=P100_55_35
            P100_45=P100_45_35
            P100_35=P100_35_35
            print("DHW AT 7°C")
            print("NOT IN USE")
            case="_DHW_35.txt"
            t_Charge_DHW3540flex1=0
            Pelec_Charge_DHW3540flex1=0
            T_TES_DHW35_flex1=0
            t_Charge_DHW3540flex2=0
            Pelec_Charge_DHW3540flex2=0
            T_TES_DHW35_flex2=0
            
            print("SH AT 7°C")
            case="_SH_35.txt"
            t_Charge_SH35flex1,Pelec_Charge_SH35flex1,T_TES_SH35_flex1=charge_no_BUH(filelocation,case,1,Mod100,Mod90,Mod70,Mod50,Mod30,T35,T45,T55,V_TES_SH,QlossSH,m_SH,T_env,rho,cp,T_SHmin,T_SHmax1,timestep,Q30_55,Q50_55,Q70_55,Q90_55,Q100_55,Q100_45,Q100_35,P30_55,P50_55,P70_55,P90_55,P100_55,P100_45,P100_35,Mod_min_Comp)
            t_Charge_SH35flex2=t_Charge_SH35flex1
            Pelec_Charge_SH35flex2=Pelec_Charge_SH35flex1
            T_TES_SH35_flex2=T_TES_SH35_flex1
  
            print("")
            
        else:
            Q30_55=Q30_55_15
            Q50_55=Q50_55_15
            Q70_55=Q70_55_15
            Q90_55=Q90_55_15
            Q100_55=Q100_55_15
            Q100_45=Q100_45_15
            Q100_35=Q100_35_15
            P30_55=P30_55_15
            P50_55=P50_55_15
            P70_55=P70_55_15
            P90_55=P90_55_15
            P100_55=P100_55_15
            P100_45=P100_45_15
            P100_35=P100_35_15
            print("DHW AT 12°C")
            print("NOT IN USE")
            case="_DHW_15.txt"
            t_Charge_DHW1540flex1=0
            Pelec_Charge_DHW1540flex1=0
            T_TES_DHW15_flex1=0
            t_Charge_DHW1540flex2=0
            Pelec_Charge_DHW1540flex2=0
            T_TES_DHW15_flex2=0
            print("SH AT 12°C")
            case="_SH_15.txt"
            t_Charge_SH15flex1,Pelec_Charge_SH15flex1,T_TES_SH15_flex1=charge_no_BUH(filelocation,case,1,Mod100,Mod90,Mod70,Mod50,Mod30,T35,T45,T55,V_TES_SH,QlossSH,m_SH,T_env,rho,cp,T_SHmin,T_SHmax1,timestep,Q30_55,Q50_55,Q70_55,Q90_55,Q100_55,Q100_45,Q100_35,P30_55,P50_55,P70_55,P90_55,P100_55,P100_45,P100_35,Mod_min_Comp)
            t_Charge_SH15flex2=t_Charge_SH15flex1
            Pelec_Charge_SH15flex2=Pelec_Charge_SH15flex1
            T_TES_SH15_flex2=T_TES_SH15_flex1
            print("")
    
    #CALCULATION OF DISCHARGING FOR SH: DISCHARGING TIME AND EXTRACTED USEFUL ENERGY
    #Discharging phase for SH at 4 outdoor temperatures, namely -7°C, 2°C, 7°C and 12°C for 2 flexibility cycles
    #print("SH discharge times for flex 1 & 2 at -7°C")
    t_Discharge_SH88flex1,Q_Discharge_SH88flex1=discharge(m_SH,V_TES_SH,QlossSH,T_env,Q35SH_88,rho,cp,T_SHmin,T_TES_SH88_flex1,timestep)
    t_Discharge_SH88flex2=t_Discharge_SH88flex1
    Q_Discharge_SH88flex2=Q_Discharge_SH88flex1
    #print("SH discharge times for flex 1 & 2 at 2°C")
    t_Discharge_SH54flex1,Q_Discharge_SH54flex1=discharge(m_SH,V_TES_SH,QlossSH,T_env,Q35SH_54,rho,cp,T_SHmin,T_TES_SH54_flex1,timestep)
    t_Discharge_SH54flex2=t_Discharge_SH54flex1
    Q_Discharge_SH54flex2=Q_Discharge_SH54flex1
    #print("SH discharge times for flex 1 & 2 at 7°C")
    t_Discharge_SH35flex1,Q_Discharge_SH35flex1=discharge(m_SH,V_TES_SH,QlossSH,T_env,Q35SH_35,rho,cp,T_SHmin,T_TES_SH35_flex1,timestep)
    t_Discharge_SH35flex2=t_Discharge_SH35flex1
    Q_Discharge_SH35flex2=Q_Discharge_SH35flex1
    #print("SH discharge times for flex 1 & 2 at 12°C")
    t_Discharge_SH15flex1,Q_Discharge_SH15flex1=discharge(m_SH,V_TES_SH,QlossSH,T_env,Q35SH_15,rho,cp,T_SHmin,T_TES_SH15_flex1,timestep)
    t_Discharge_SH15flex2=t_Discharge_SH15flex1
    Q_Discharge_SH15flex2=Q_Discharge_SH15flex1

    #CALCULATION OF DISCHARGING FOR DHW: DISCHARGING TIME AND USEFUL ENERGY
    #DHW discharge times for flex 1 & 2 at reduced day
    treduced_Discharge_DHW_88_flex1=0
    Qreduced_Discharge_DHW_88_flex1=0
    treduced_Discharge_DHW_88_flex2=0
    Qreduced_Discharge_DHW_88_flex2=0
    treduced_Discharge_DHW_54_flex1=0
    Qreduced_Discharge_DHW_54_flex1=0
    treduced_Discharge_DHW_54_flex2=0
    Qreduced_Discharge_DHW_54_flex2=0
    treduced_Discharge_DHW_35_flex1=0
    Qreduced_Discharge_DHW_35_flex1=0
    treduced_Discharge_DHW_35_flex2=0
    Qreduced_Discharge_DHW_35_flex2=0
    treduced_Discharge_DHW_15_flex1=0
    Qreduced_Discharge_DHW_15_flex1=0
    treduced_Discharge_DHW_15_flex2=0
    Qreduced_Discharge_DHW_15_flex2=0
    
    writeresultfile=open(resultfile,'w')   
    writeresultfile.write("DHW charging time at 12 °C for Flex1 (minutes)"+'\t'+str(t_Charge_DHW1540flex1)+'\n') 
    writeresultfile.write("DHW charging time at 12 °C for Flex2 (minutes)"+'\t'+str(t_Charge_DHW1540flex2)+'\n') 
    writeresultfile.write("DHW charging time at 7 °C for Flex1 (minutes)"+'\t'+str(t_Charge_DHW3540flex1)+'\n') 
    writeresultfile.write("DHW charging time at 7 °C for Flex2 (minutes)"+'\t'+str(t_Charge_DHW3540flex2)+'\n')
    writeresultfile.write("DHW charging time at 2 °C for Flex1 (minutes)"+'\t'+str(t_Charge_DHW5440flex1)+'\n') 
    writeresultfile.write("DHW charging time at 2 °C for Flex2 (minutes)"+'\t'+str(t_Charge_DHW5440flex2)+'\n')
    writeresultfile.write("DHW charging time at -7 °C for Flex1 (minutes)"+'\t'+str(t_Charge_DHW8840flex1)+'\n')
    writeresultfile.write("DHW charging time at -7 °C for Flex2 (minutes)"+'\t'+str(t_Charge_DHW8840flex2)+'\n') 
    
    writeresultfile.write("SH charging time at 12 °C for Flex1 (minutes)"+'\t'+str(t_Charge_SH15flex1)+'\n') 
    writeresultfile.write("SH charging time at 12 °C for Flex2 (minutes)"+'\t'+str(t_Charge_SH15flex2)+'\n')
    writeresultfile.write("SH charging time at 7 °C for Flex1 (minutes)"+'\t'+str(t_Charge_SH35flex1)+'\n')
    writeresultfile.write("SH charging time at 7 °C for Flex2 (minutes)"+'\t'+str(t_Charge_SH35flex2)+'\n')
    writeresultfile.write("SH charging time at 2 °C for Flex1 (minutes)"+'\t'+str(t_Charge_SH54flex1)+'\n')
    writeresultfile.write("SH charging time at 2 °C for Flex2 (minutes)"+'\t'+str(t_Charge_SH54flex2)+'\n')
    writeresultfile.write("SH charging time at -7 °C for Flex1 (minutes)"+'\t'+str(t_Charge_SH88flex1)+'\n')
    writeresultfile.write("SH charging time at -7 °C for Flex2 (minutes)"+'\t'+str(t_Charge_SH88flex2)+'\n')
    
    writeresultfile.write("DHW discharging time at 12 °C for Flex1 (minutes)"+'\t'+str(treduced_Discharge_DHW_15_flex1)+'\n')
    writeresultfile.write("DHW discharging time at 12 °C for Flex2 (minutes)"+'\t'+str(treduced_Discharge_DHW_15_flex2)+'\n')
    writeresultfile.write("DHW discharging time at 7 °C for Flex1 (minutes)"+'\t'+str(treduced_Discharge_DHW_35_flex1)+'\n')
    writeresultfile.write("DHW discharging time at 7 °C for Flex2 (minutes)"+'\t'+str(treduced_Discharge_DHW_35_flex2)+'\n')
    writeresultfile.write("DHW discharging time at 2 °C for Flex1 (minutes)"+'\t'+str(treduced_Discharge_DHW_54_flex1)+'\n')
    writeresultfile.write("DHW discharging time at 2 °C for Flex2 (minutes)"+'\t'+str(treduced_Discharge_DHW_54_flex2)+'\n')
    writeresultfile.write("DHW discharging time at -7 °C for Flex1 (minutes)"+'\t'+str(treduced_Discharge_DHW_88_flex1)+'\n')
    writeresultfile.write("DHW discharging time at -7 °C for Flex2 (minutes)"+'\t'+str(treduced_Discharge_DHW_88_flex2)+'\n')
    
    writeresultfile.write("SH discharging time at 12 °C for Flex1 (minutes)"+'\t'+str(t_Discharge_SH15flex1)+'\n')
    writeresultfile.write("SH discharging time at 12 °C for Flex2 (minutes)"+'\t'+str(t_Discharge_SH15flex2)+'\n')
    writeresultfile.write("SH discharging time at 7 °C for Flex1 (minutes)"+'\t'+str(t_Discharge_SH35flex1)+'\n')
    writeresultfile.write("SH discharging time at 7 °C for Flex2 (minutes)"+'\t'+str(t_Discharge_SH35flex2)+'\n')
    writeresultfile.write("SH discharging time at 2 °C for Flex1 (minutes)"+'\t'+str(t_Discharge_SH54flex1)+'\n')
    writeresultfile.write("SH discharging time at 2 °C for Flex2 (minutes)"+'\t'+str(t_Discharge_SH54flex2)+'\n')
    writeresultfile.write("SH discharging time at -7 °C for Flex1 (minutes)"+'\t'+str(t_Discharge_SH88flex1)+'\n')   
    writeresultfile.write("SH discharging time at -7 °C for Flex2 (minutes)"+'\t'+str(t_Discharge_SH88flex2)+'\n')  

    writeresultfile.write("DHW thermal energy at 12 °C for Flex1 (kWh_th)"+'\t'+str(Qreduced_Discharge_DHW_15_flex1)+'\n')
    writeresultfile.write("DHW thermal energy at 12 °C for Flex2 (kWh_th)"+'\t'+str(Qreduced_Discharge_DHW_15_flex2)+'\n')
    writeresultfile.write("DHW thermal energy at 7 °C for Flex1 (kWh_th)"+'\t'+str(Qreduced_Discharge_DHW_35_flex1)+'\n')
    writeresultfile.write("DHW thermal energy at 7 °C for Flex2 (kWh_th)"+'\t'+str(Qreduced_Discharge_DHW_35_flex2)+'\n')    
    writeresultfile.write("DHW thermal energy at 2 °C for Flex1 (kWh_th)"+'\t'+str(Qreduced_Discharge_DHW_54_flex1)+'\n')
    writeresultfile.write("DHW thermal energy at 2 °C for Flex2 (kWh_th)"+'\t'+str(Qreduced_Discharge_DHW_54_flex2)+'\n')
    writeresultfile.write("DHW thermal energy at -7 °C for Flex1 (kWh_th)"+'\t'+str(Qreduced_Discharge_DHW_88_flex1)+'\n')
    writeresultfile.write("DHW thermal energy at -7 °C for Flex2 (kWh_th)"+'\t'+str(Qreduced_Discharge_DHW_88_flex2)+'\n')
    
    writeresultfile.write("SH thermal energy at 12 °C for Flex1 (kWh_th)"+'\t'+str(Q_Discharge_SH15flex1)+'\n')
    writeresultfile.write("SH thermal energy at 12 °C for Flex2 (kWh_th)"+'\t'+str(Q_Discharge_SH15flex2)+'\n')
    writeresultfile.write("SH thermal energy at 7 °C for Flex1 (kWh_th)"+'\t'+str(Q_Discharge_SH35flex1)+'\n')
    writeresultfile.write("SH thermal energy at 7 °C for Flex2 (kWh_th)"+'\t'+str(Q_Discharge_SH35flex2)+'\n')  
    writeresultfile.write("SH thermal energy at 2 °C for Flex1 (kWh_th)"+'\t'+str(Q_Discharge_SH54flex1)+'\n')
    writeresultfile.write("SH thermal energy at 2 °C for Flex2 (kWh_th)"+'\t'+str(Q_Discharge_SH54flex2)+'\n')
    writeresultfile.write("SH thermal energy at -7 °C for Flex1 (kWh_th)"+'\t'+str(Q_Discharge_SH88flex1)+'\n')
    writeresultfile.write("SH thermal energy at -7 °C for Flex2 (kWh_th)"+'\t'+str(Q_Discharge_SH88flex2)+'\n')
    
    writeresultfile.write("DHW electrical energy at 12 °C for Flex1 (kWh_e)"+'\t'+str(Pelec_Charge_DHW1540flex1/3600000)+'\n')
    writeresultfile.write("DHW electrical energy at 12 °C for Flex2 (kWh_e)"+'\t'+str(Pelec_Charge_DHW1540flex2/3600000)+'\n')
    writeresultfile.write("DHW electrical energy at 7 °C for Flex1 (kWh_e)"+'\t'+str(Pelec_Charge_DHW1540flex1/3600000)+'\n')
    writeresultfile.write("DHW electrical energy at 7 °C for Flex2 (kWh_e)"+'\t'+str(Pelec_Charge_DHW3540flex2/3600000)+'\n')  
    writeresultfile.write("DHW electrical energy at 2 °C for Flex1 (kWh_e)"+'\t'+str(Pelec_Charge_DHW5440flex1/3600000)+'\n')
    writeresultfile.write("DHW electrical energy at 2 °C for Flex2 (kWh_e)"+'\t'+str(Pelec_Charge_DHW5440flex2/3600000)+'\n')
    writeresultfile.write("DHW electrical energy at -7 °C for Flex1 (kWh_e)"+'\t'+str(Pelec_Charge_DHW8840flex1/3600000)+'\n')
    writeresultfile.write("DHW electrical energy at -7 °C for Flex2 (kWh_e)"+'\t'+str(Pelec_Charge_DHW8840flex2/3600000)+'\n')  
    
    writeresultfile.write("SH electrical energy at 12 °C for Flex1 (kWh_e)"+'\t'+str(Pelec_Charge_SH15flex1/3600000)+'\n')
    writeresultfile.write("SH electrical energy at 12 °C for Flex2 (kWh_e)"+'\t'+str(Pelec_Charge_SH15flex2/3600000)+'\n') 
    writeresultfile.write("SH electrical energy at 7 °C for Flex1 (kWh_e)"+'\t'+str(Pelec_Charge_SH35flex1/3600000)+'\n') 
    writeresultfile.write("SH electrical energy at 7 °C for Flex2 (kWh_e)"+'\t'+str(Pelec_Charge_SH35flex2/3600000)+'\n') 
    writeresultfile.write("SH electrical energy at 2 °C for Flex1 (kWh_e)"+'\t'+str(Pelec_Charge_SH54flex1/3600000)+'\n') 
    writeresultfile.write("SH electrical energy at 2 °C for Flex2 (kWh_e)"+'\t'+str(Pelec_Charge_SH54flex2/3600000)+'\n') 
    writeresultfile.write("SH electrical energy at -7 °C for Flex1 (kWh_e)"+'\t'+str(Pelec_Charge_SH88flex1/3600000)+'\n') 
    writeresultfile.write("SH electrical energy at -7 °C for Flex2 (kWh_e)"+'\t'+str(Pelec_Charge_SH88flex2/3600000)+'\n')     

    print("\n---------------------------------------------------------")  
    print("RESULTS:")  
    print("\n")  
    
    tflex1=(t_Charge_DHW1540flex1+t_Charge_SH15flex1+t_Charge_DHW3540flex1+t_Charge_SH35flex1+t_Charge_DHW5440flex1+t_Charge_SH54flex1+t_Charge_DHW8840flex1+t_Charge_SH88flex1+t_Discharge_SH88flex1+t_Discharge_SH54flex1+t_Discharge_SH35flex1+t_Discharge_SH15flex1+treduced_Discharge_DHW_88_flex1+treduced_Discharge_DHW_54_flex1+treduced_Discharge_DHW_35_flex1+treduced_Discharge_DHW_15_flex1)/4
    tflex2=(t_Charge_DHW1540flex2+t_Charge_SH15flex2+t_Charge_DHW3540flex2+t_Charge_SH35flex2+t_Charge_DHW5440flex2+t_Charge_SH54flex2+t_Charge_DHW8840flex2+t_Charge_SH88flex2+t_Discharge_SH88flex2+t_Discharge_SH54flex2+t_Discharge_SH35flex2+t_Discharge_SH15flex2+treduced_Discharge_DHW_88_flex2+treduced_Discharge_DHW_54_flex2+treduced_Discharge_DHW_35_flex2+treduced_Discharge_DHW_15_flex2)/4
    writeresultfile.write("tflex1 (minutes)"+'\t'+str(tflex1)+'\n') 
    writeresultfile.write("tflex2 (minutes)"+'\t'+str(tflex2)+'\n') 
    
    print("   tflex1 = " +str(round(tflex1,2)) +str(" minutes"))
    print("   tflex2 = " +str(round(tflex2,2)) +str(" minutes"))
    print("\n---------------------------------------------------------")  
    
    Quseful_flex1=(Qreduced_Discharge_DHW_88_flex1+Qreduced_Discharge_DHW_54_flex1+Qreduced_Discharge_DHW_35_flex1+Qreduced_Discharge_DHW_15_flex1+Q_Discharge_SH15flex1+Q_Discharge_SH35flex1+Q_Discharge_SH54flex1+Q_Discharge_SH88flex1)/4
    Quseful_flex2=(Qreduced_Discharge_DHW_88_flex2+Qreduced_Discharge_DHW_54_flex2+Qreduced_Discharge_DHW_35_flex2+Qreduced_Discharge_DHW_15_flex2+Q_Discharge_SH15flex2+Q_Discharge_SH35flex2+Q_Discharge_SH54flex2+Q_Discharge_SH88flex2)/4
    writeresultfile.write("Quseful_flex1 (kWh_th)"+'\t'+str(Quseful_flex1)+'\n') 
    writeresultfile.write("Quseful_flex2 (kWh_th)"+'\t'+str(Quseful_flex2)+'\n') 

    print("   Quseful_flex1 = " +str(round(Quseful_flex1,2)) +str(" kWh_th"))
    print("   Quseful_flex2 = " +str(round(Quseful_flex2,2)) +str(" kWh_th"))
    print("\n---------------------------------------------------------")       
    
    Pelec_flex1=(Pelec_Charge_DHW1540flex1+Pelec_Charge_SH15flex1+Pelec_Charge_DHW3540flex1+Pelec_Charge_SH35flex1+Pelec_Charge_DHW5440flex1+Pelec_Charge_SH54flex1+Pelec_Charge_DHW8840flex1+Pelec_Charge_SH88flex1)/(4*3600000)
    Pelec_flex2=(Pelec_Charge_DHW1540flex2+Pelec_Charge_SH15flex2+Pelec_Charge_DHW3540flex2+Pelec_Charge_SH35flex2+Pelec_Charge_DHW5440flex2+Pelec_Charge_SH54flex2+Pelec_Charge_DHW8840flex2+Pelec_Charge_SH88flex2)/(4*3600000)
    writeresultfile.write("Pelec_flex1 (kWh_e)"+'\t'+str(Pelec_flex1)+'\n') 
    writeresultfile.write("Pelec_flex2 (kWh_e)"+'\t'+str(Pelec_flex2)+'\n') 

    print("   Pelec_flex1 = " +str(round(Pelec_flex1,2)) +str(" kWh_e"))
    print("   Pelec_flex2 = " +str(round(Pelec_flex2,2)) +str(" kWh_e"))
    print("\n---------------------------------------------------------")  
    
    COP_flex1=Quseful_flex1/Pelec_flex1
    COP_flex2=Quseful_flex2/Pelec_flex2
    writeresultfile.write("COP_flex1 (-)"+'\t'+str(COP_flex1)+'\n') 
    writeresultfile.write("COP_flex2 (-)"+'\t'+str(COP_flex2)+'\n') 
    
    print("   COP_flex1 = " +str(round(COP_flex1,2)))
    print("   COP_flex2 = " +str(round(COP_flex2,2)))
    print("\n---------------------------------------------------------")  
    
    Quseful_DHW=(Qreduced_Discharge_DHW_88_flex1+Qreduced_Discharge_DHW_54_flex1+Qreduced_Discharge_DHW_35_flex1+Qreduced_Discharge_DHW_15_flex1+Qreduced_Discharge_DHW_88_flex2+Qreduced_Discharge_DHW_54_flex2+Qreduced_Discharge_DHW_35_flex2+Qreduced_Discharge_DHW_15_flex2)/4
    Quseful_SH=(Q_Discharge_SH15flex1+Q_Discharge_SH35flex1+Q_Discharge_SH54flex1+Q_Discharge_SH88flex1+Q_Discharge_SH15flex2+Q_Discharge_SH35flex2+Q_Discharge_SH54flex2+Q_Discharge_SH88flex2)/4
    Quseful_total=Quseful_DHW+Quseful_SH
    writeresultfile.write("Share of DHW service in total thermal energy (%)"+'\t'+str(100*Quseful_DHW/Quseful_total)+'\n') 
    writeresultfile.write("Share of SH service in total thermal energy (%)"+'\t'+str(100*Quseful_SH/Quseful_total)+'\n') 
    
    print("   Quseful_DHW   = " +str(round(Quseful_DHW,2)) +str(" kWh_th"))
    print("   Quseful_SH    = " +str(round(Quseful_SH,2)) +str(" kWh_th"))
    print("   Quseful_total = " +str(round(Quseful_total,2)) +str(" kWh_th"))
    print("\n---------------------------------------------------------")   
    
    COPref=COP35SH_ref
    writeresultfile.write("Reference COP (-)"+'\t'+str(COPref)+'\n') 
    
    print("   Reference COP = " +str(round(COPref,2)))
    print("\n---------------------------------------------------------")  
    
    Eff_flex=((tflex1*(COP_flex1/COPref))+(tflex2*(COP_flex2/COPref)))/(tflex1+tflex2)
    writeresultfile.write("Efficiency of the overall flexibility provision (%)"+'\t'+str(100*Eff_flex)+'\n') 
    
    print("   Efficiency of the overall flexibility provision = " +str(100*round(Eff_flex,4))+ str(" %"))
    print("\n---------------------------------------------------------")  
    
    tcharge_total=(t_Charge_DHW1540flex1+t_Charge_SH15flex1+t_Charge_DHW3540flex1+t_Charge_SH35flex1+t_Charge_DHW5440flex1+t_Charge_SH54flex1+t_Charge_DHW8840flex1+t_Charge_SH88flex1+t_Charge_DHW1540flex2+t_Charge_SH15flex2+t_Charge_DHW3540flex2+t_Charge_SH35flex2+t_Charge_DHW5440flex2+t_Charge_SH54flex2+t_Charge_DHW8840flex2+t_Charge_SH88flex2)/8
    tdischarge_total=(t_Discharge_SH88flex1+t_Discharge_SH54flex1+t_Discharge_SH35flex1+t_Discharge_SH15flex1+t_Discharge_SH88flex2+t_Discharge_SH54flex2+t_Discharge_SH35flex2+t_Discharge_SH15flex2+treduced_Discharge_DHW_88_flex1+treduced_Discharge_DHW_54_flex1+treduced_Discharge_DHW_35_flex1+treduced_Discharge_DHW_15_flex1+treduced_Discharge_DHW_88_flex2+treduced_Discharge_DHW_54_flex2+treduced_Discharge_DHW_35_flex2+treduced_Discharge_DHW_15_flex2)/8   
    writeresultfile.write("Total average charging time (minutes)"+'\t'+str(tcharge_total)+'\n') 
    writeresultfile.write("Total average discharging time (minutes)"+'\t'+str(tdischarge_total)+'\n') 
    writeresultfile.close()
    
    print("   Total average charging time   = " +str(round(tcharge_total,2)) +str(" minutes"))
    print("   Total average discharging time = " +str(round(tdischarge_total,2)) +str(" minutes"))
    print("\n---------------------------------------------------------")  
"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def discharge(flow,V,Ploss,Tenv,Qload,rho,cp,Tmin,Tmax,dt):
    b=(Tmin-5,Tmax+5)
    TESbnds=(b,b,b,b,b,b,b,b,b,b)
    Ploss=Ploss/nseg
    m=(V*rho)/nseg
    Told=[Tmax]*nseg
    Told_intermediate=Told
    Tloadin_intermediate=Told[0]
    Tloadin=Told[0]
    NumberMin=0
    Tavg=0
    for i in range(nseg):
        Tavg=Tavg+Told[i]
    Tavg=Tavg/nseg
    while Tavg>Tmin:
        Told=Told_intermediate
        Tloadin=Tloadin_intermediate
        Tloadreturn=Tloadin-(Qload/(flow*cp))
        Told_intermediate,Tloadin_intermediate=dTES_singlestep(Tloadreturn,Told,m,cp,dt,flow,Ploss,Tenv,TESbnds,nseg)
        Tavg=0
        for i in range(nseg):
            Tavg=Tavg+Told_intermediate[i]
        Tavg=Tavg/nseg
        NumberMin=NumberMin+1
    #Import needed python packages
    import numpy as np
    from scipy.optimize import minimize_scalar
    def objective(x):
        Told_intermediate,Tloadin_intermediate=dTES_singlestep(Tloadreturn,Told,m,cp,x,flow,Ploss,Tenv,TESbnds,nseg)
        Tavg=0
        for i in range(nseg):
            Tavg=Tavg+Told_intermediate[i]
        Tavg=Tavg/nseg
        return (((Tavg-Tmin)**2)**0.5)
    #Start-value as an input to the objective function
    x0=0.75*dt
    objective(x0)

    #Boundaries
    b=(0,dt)
    bnds=(b)

    #Minimise Python function
    sol=minimize_scalar(objective,x0,method='bounded',bounds=bnds,options={'xatol':1e-08,'maxiter':10000}) 
    dtlast=sol.x
    FinalTime=(dt*NumberMin+dtlast)/dt
    Quse=((FinalTime)*dt*Qload)/3600000
    return ((dt*FinalTime)/60),Quse
"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def charge_no_BUH(filelocation,case,Mode,Mod100,Mod90,Mod70,Mod50,Mod30,T35,T45,T55,V,Ploss,flow,Tenv,rho,c,Tmin,Tmax,dt,Q30_55,Q50_55,Q70_55,Q90_55,Q100_55,Q100_45,Q100_35,P30_55,P50_55,P70_55,P90_55,P100_55,P100_45,P100_35,Mod_min_Comp):
    import numpy as np
    checkvalue=0
    Pconsumed=0
    TotalTime=0
    T_TES=Tmin
    Tavg_TES=Tmin
    m=(V*rho)/nseg
    #Temperatures at each layer, Told holds the TES temperatures for each segment at time t and Tnew at time (t+dt)
    Told=[Tmin]*nseg
    TES_Tlayers=[Tmin]*nseg
    TESb=(Tmin-5,Tmax+5)
    TESbnds=(TESb,TESb,TESb,TESb,TESb,TESb,TESb,TESb,TESb,TESb)
    Ploss=Ploss/nseg
    
    if Mode==0:
        filename=filelocation+"Charge_DHW_no_BUH"+case
        writefile=open(filename,'w')
    else:
        filename=filelocation+"Charge_SH_no_BUH"+case 
        writefile=open(filename,'w')
    writefile.write("Time (s)"+'\t'+"T_HP_in (°C)"+'\t'+"Q_HP (W_th)"+'\t'+"P_HP (W_e)"+'\t'+"Modulation_Comp (-)"+'\t'+"Modulation_BUH (-)"+'\t'+"T_HP_out (°C)"+'\t'+"COP (-)"+'\n')
    writefile.write(str(TotalTime)+'\t'+str(T_TES)+'\t'+str(0)+'\t'+str(0)+'\t'+str(0)+'\t'+str(0)+'\t'+str(0)+'\t'+str(0)+'\n')
    while checkvalue==0:
        share_low,share_high,T_TES,checkvalue,Pelec,ModPerc,QHPsup,THPSup,Tavg_inter,Tnew=charge_full_load_no_BUH(Tenv,Ploss,Q100_35,Q100_45,P100_35,P100_45,T35,T45,V,c,flow,rho,dt,T_TES,m,TESbnds,Told)
        Pconsumed=Pconsumed+Pelec*dt
        if checkvalue==0:
            Told=Tnew
            Tavg_TES=Tavg_inter
            TotalTime=TotalTime+dt
            TES_Tlayers=np.vstack((TES_Tlayers,Told))
            #print(TotalTime," Full load: ",Told)
            writefile.write(str(TotalTime)+'\t'+str(T_TES)+'\t'+str(QHPsup)+'\t'+str(Pelec)+'\t'+str(ModPerc)+'\t'+str(0)+'\t'+str(THPSup)+'\t'+str(QHPsup/Pelec)+'\n')
    checkvalue=0
    while checkvalue==0:
        share_low,share_high,T_TES,checkvalue,Pelec,ModPerc,QHPsup,THPSup,Tavg_inter,Tnew=charge_full_load_no_BUH(Tenv,Ploss,Q100_45,Q100_55,P100_45,P100_55,T45,T55,V,c,flow,rho,dt,T_TES,m,TESbnds,Told)
        Pconsumed=Pconsumed+Pelec*dt
        if checkvalue==0:
            Told=Tnew
            Tavg_TES=Tavg_inter
            TotalTime=TotalTime+dt    
            TES_Tlayers=np.vstack((TES_Tlayers,Told))
            #print(TotalTime," Full load: ",Told)
            writefile.write(str(TotalTime)+'\t'+str(T_TES)+'\t'+str(QHPsup)+'\t'+str(Pelec)+'\t'+str(ModPerc)+'\t'+str(0)+'\t'+str(THPSup)+'\t'+str(QHPsup/Pelec)+'\n')          
    checkvalue=0  
    while checkvalue==0:
        share_low,share_high,T_TES,checkvalue,Pelec,ModPerc,QHPsup,THPSup,Tavg_inter,Tnew=charge_part_load_no_BUH(Mod100,Mod90,Tenv,Ploss,Q100_55,Q90_55,P100_55,P90_55,T55,V,c,flow,rho,dt,T_TES,m,TESbnds,Told)
        Pconsumed=Pconsumed+Pelec*dt
        if checkvalue==0:
            Told=Tnew
            Tavg_TES=Tavg_inter
            TotalTime=TotalTime+dt
            TES_Tlayers=np.vstack((TES_Tlayers,Told))
            #print(TotalTime," Part load: ",Told)
            writefile.write(str(TotalTime)+'\t'+str(T_TES)+'\t'+str(QHPsup)+'\t'+str(Pelec)+'\t'+str(ModPerc)+'\t'+str(0)+'\t'+str(THPSup)+'\t'+str(QHPsup/Pelec)+'\n')
    checkvalue=0
    while checkvalue==0:
        share_low,share_high,T_TES,checkvalue,Pelec,ModPerc,QHPsup,THPSup,Tavg_inter,Tnew=charge_part_load_no_BUH(Mod90,Mod70,Tenv,Ploss,Q90_55,Q70_55,P90_55,P70_55,T55,V,c,flow,rho,dt,T_TES,m,TESbnds,Told)
        Pconsumed=Pconsumed+Pelec*dt
        if checkvalue==0:
            Told=Tnew
            Tavg_TES=Tavg_inter
            TotalTime=TotalTime+dt
            TES_Tlayers=np.vstack((TES_Tlayers,Told))
            #print(TotalTime," Part load: ",Told)
            writefile.write(str(TotalTime)+'\t'+str(T_TES)+'\t'+str(QHPsup)+'\t'+str(Pelec)+'\t'+str(ModPerc)+'\t'+str(0)+'\t'+str(THPSup)+'\t'+str(QHPsup/Pelec)+'\n')
    checkvalue=0  
    while checkvalue==0:  
        share_low,share_high,T_TES,checkvalue,Pelec,ModPerc,QHPsup,THPSup,Tavg_inter,Tnew=charge_part_load_no_BUH(Mod70,Mod50,Tenv,Ploss,Q70_55,Q50_55,P70_55,P50_55,T55,V,c,flow,rho,dt,T_TES,m,TESbnds,Told)
        Pconsumed=Pconsumed+Pelec*dt
        if checkvalue==0:
            Told=Tnew
            Tavg_TES=Tavg_inter
            TotalTime=TotalTime+dt
            TES_Tlayers=np.vstack((TES_Tlayers,Told))
            #print(TotalTime," Part load: ",Told)
            writefile.write(str(TotalTime)+'\t'+str(T_TES)+'\t'+str(QHPsup)+'\t'+str(Pelec)+'\t'+str(ModPerc)+'\t'+str(0)+'\t'+str(THPSup)+'\t'+str(QHPsup/Pelec)+'\n')
    checkvalue=0    
    while checkvalue==0:       
        share_low,share_high,T_TES,checkvalue,Pelec,ModPerc,QHPsup,THPSup,Tavg_inter,Tnew=charge_part_load_no_BUH(Mod50,Mod30,Tenv,Ploss,Q50_55,Q30_55,P50_55,P30_55,T55,V,c,flow,rho,dt,T_TES,m,TESbnds,Told)
        Pconsumed=Pconsumed+Pelec*dt
        if checkvalue==0:
            Told=Tnew
            Tavg_TES=Tavg_inter
            TotalTime=TotalTime+dt
            TES_Tlayers=np.vstack((TES_Tlayers,Told))
            #print(TotalTime," Part load: ",Told)
            writefile.write(str(TotalTime)+'\t'+str(T_TES)+'\t'+str(QHPsup)+'\t'+str(Pelec)+'\t'+str(ModPerc)+'\t'+str(0)+'\t'+str(THPSup)+'\t'+str(QHPsup/Pelec)+'\n')
    checkvalue=0   
    while checkvalue==0:
        T_TES,checkvalue,Pelec,ModPerc,timelapse,QHPsup,THPSup,Tavg_inter,Tnew=charge_minload_no_BUH(Mod_min_Comp,Tenv,Ploss,Q30_55,P30_55,Tmax,V,c,flow,rho,dt,T_TES,m,TESbnds,Told) 
        Pconsumed=Pconsumed+Pelec*timelapse
        if checkvalue==0:
            Told=Tnew
            Tavg_TES=Tavg_inter
            TotalTime=TotalTime+timelapse
            TES_Tlayers=np.vstack((TES_Tlayers,Told))
            #print(TotalTime," Min load: ",Told)
            writefile.write(str(TotalTime)+'\t'+str(T_TES)+'\t'+str(QHPsup)+'\t'+str(Pelec)+'\t'+str(ModPerc)+'\t'+str(0)+'\t'+str(THPSup)+'\t'+str(QHPsup/Pelec)+'\n')
        if checkvalue==2:
            Told=Tnew
            Tavg_TES=Tavg_inter
            TotalTime=TotalTime+timelapse
            TES_Tlayers=np.vstack((TES_Tlayers,Told))
            #print(TotalTime," Last at Min load: ",Told)
            writefile.write(str(TotalTime)+'\t'+str(T_TES)+'\t'+str(QHPsup)+'\t'+str(Pelec)+'\t'+str(ModPerc)+'\t'+str(0)+'\t'+str(THPSup)+'\t'+str(QHPsup/Pelec)+'\n')
    writefile.close()
    #print("ELEC")
    #print(Pconsumed/3600000)
    #print("Time")
    TotalTime=TotalTime/60
    #print(TotalTime)
    return TotalTime,Pconsumed,Tavg_TES
"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""" 
def charge_full_load_no_BUH(Tenv,Ploss,Qlow,Qhigh,Plow,Phigh,Tlow,Thigh,V,c,flow,rho,dt,T_TES,m,TESbnds,Tprevstep):
    #Import needed python packages
    import numpy as np
    from scipy.optimize import minimize_scalar
    
    #Define the objective function: this is the function to minimise/optimise
    def objective(x):
        Tcalc= x*Tlow+(1-x)*Thigh
        QHPcalc=x*Qlow+(1-x)*Qhigh
        dt_increase=QHPcalc/(flow*c)
        Tsup=T_TES+dt_increase
        return (((Tcalc-Tsup)**2)**0.5)
    
    #Start-value as an input to the objective function
    x0=0.75
    objective(x0)
    
    #Boundaries
    b=(-0.1,1.1)
    bnds=(b)
    
    #Minimise Python function
    sol=minimize_scalar(objective,x0,method='bounded',bounds=bnds,options={'xatol':1e-08,'maxiter':10000})  
    
    #Notcor equal to 1 means a fault calculation
    notcor=0
    Pelec=0
    ModPerc=0
    QHPsup=0
    
    #Share calculation
    share_low=sol.x
    share_high=1-share_low
    
    #Calculation of HP Supply Temperature
    THPSupply=T_TES+((share_low*Qlow+share_high*Qhigh)/(c*flow))
    
    #Fault result detection: happens if out of the boundaries
    if share_low<0 or share_low>1:
        notcor=1
        TendTES=T_TES
        Told=Tprevstep
    elif share_high<0 or share_high>1:
        print("Invalid")
        notcor=1
        TendTES=T_TES
        Told=Tprevstep
    elif (THPSupply)>Thigh:
        print("Invalid")
        notcor=1
        TendTES=T_TES
        Told=Tprevstep
    else:
        Told,THPreturn=TES_singlestep(THPSupply,Tprevstep,m,c,dt,flow,Ploss,Tenv,TESbnds,nseg)
        TendTES=Told[nseg-1]
        QHPsup=share_low*Qlow+share_high*Qhigh
        Pelec=share_low*Plow+share_high*Phigh
        ModPerc=1
    Tavg=0
    for i in range(nseg):
        Tavg=Tavg+Told[i]
    Tavg=Tavg/nseg         
    return share_low,share_high,TendTES,notcor,Pelec,ModPerc,QHPsup,THPSupply,Tavg,Told
"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def charge_part_load_no_BUH(ModLow,ModHigh,Tenv,Ploss,Qlow,Qhigh,Plow,Phigh,TSet,V,c,flow,rho,dt,T_TES,m,TESbnds,Tprevstep):  
    import numpy as np
    from scipy.optimize import minimize_scalar
    
    def objective(x):
        Tcalc=TSet
        QHPcalc=x*Qlow+(1-x)*Qhigh
        dt_increase=QHPcalc/(flow*c)
        Tsup=T_TES+dt_increase
        return (((Tcalc-Tsup)**2)**0.5)
    
    x0=0.75
    objective(x0)
    
    b=(-0.1,1.1)
    bnds=(b)
 
    sol=minimize_scalar(objective,x0,method='bounded',bounds=bnds,options={'xatol':1e-08,'maxiter':10000})    

    notcor=0
    Pelec=0
    ModPerc=0
    QHPsup=0
    
    share_low=sol.x
    share_high=1-share_low

    THPSupply=T_TES+((share_low*Qlow+share_high*Qhigh)/(c*flow))
    if share_low<0 or share_low>1:
        notcor=1
        TendTES=T_TES
        Told=Tprevstep
    elif share_high<0 or share_high>1:
        print("Invalid")
        notcor=1
        TendTES=T_TES
        Told=Tprevstep
    elif (THPSupply)>(TSet+0.001):
        print("Invalid")
        notcor=1
        TendTES=T_TES
        Told=Tprevstep
    else:
        Told,THPreturn=TES_singlestep(THPSupply,Tprevstep,m,c,dt,flow,Ploss,Tenv,TESbnds,nseg)
        TendTES=Told[nseg-1]
        QHPsup=share_low*Qlow+share_high*Qhigh   
        Pelec=share_low*Plow+share_high*Phigh
        ModPerc=share_low*ModLow+share_high*ModHigh
    Tavg=0
    for i in range(nseg):
        Tavg=Tavg+Told[i]
    Tavg=Tavg/nseg  
    return share_low,share_high,TendTES,notcor,Pelec,ModPerc,QHPsup,THPSupply,Tavg,Told
"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""   
def charge_minload_no_BUH(Mod_min_Comp,Tenv,Ploss,Qmincharge,Pmincharge,TSet,V,c,flow,rho,dt,T_TES,m,TESbnds,Tprevstep):  
    QHPsup=Qmincharge
    THPSupply=T_TES+((Qmincharge)/(c*flow))
    notcor=0
    Pelec=Pmincharge
    ModPerc=Mod_min_Comp
    timelapse=dt
    if (THPSupply)>(TSet+5):
        print("The compressor supply temperature was 5°C higher compared to its maximum temperature.")
        print("Therefore, the storage will not be fully charged.")
        Told=Tprevstep
        notcor=2
        TendTES=T_TES  
        Pelec=0
        timelapse=0
        QHPsup=0
        ModPerc=0
    else:       
        #Check if working on minimum modulation for full time step is possible or not
        Told_intermediate,THPreturn=TES_singlestep(THPSupply,Tprevstep,m,c,dt,flow,Ploss,Tenv,TESbnds,nseg)
        Tavg=0
        for i in range(nseg):
            Tavg=Tavg+Told_intermediate[i]
        Tavg=Tavg/nseg
        if Tavg<TSet:
            TendTES=Told_intermediate[nseg-1]
            Told=Told_intermediate
        else:      
            import numpy as np
            from scipy.optimize import minimize_scalar
            def objective(x):
                Told_intermediate,THPreturn=TES_singlestep(THPSupply,Tprevstep,m,c,x,flow,Ploss,Tenv,TESbnds,nseg)
                Tavg=0
                for i in range(nseg):
                    Tavg=Tavg+Told_intermediate[i]
                Tavg=Tavg/nseg
                return (((Tavg-TSet)**2)**0.5)               
            x0=0.75
            objective(x0)
            b=(0,dt)
            bnds=(b)
            sol=minimize_scalar(objective,x0,method='bounded',bounds=bnds,options={'xatol':1e-08,'maxiter':10000})   
            timelapse=sol.x
            Told,THPreturn=TES_singlestep(THPSupply,Tprevstep,m,c,timelapse,flow,Ploss,Tenv,TESbnds,nseg)
            TendTES=Told[nseg-1]
            notcor=2         
            print("SUCCESSFUL")
    Tavg=0
    for i in range(nseg):
        Tavg=Tavg+Told[i]
    Tavg=Tavg/nseg  
    return TendTES,notcor,Pelec,ModPerc,timelapse,QHPsup,THPSupply,Tavg,Told
"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def TES_singlestep(THPCond,Tprevious,m,c,dt,flow,Qloss,Tenv,TESbnds,nseg):
    Ttry=[0]*10
    Ttry[0]=((-(flow*c*Tprevious[0])+(flow*c*THPCond)-(Qloss*(Tprevious[0]-Tenv)))*(dt/(m*c)))+Tprevious[0]
    Ttry[1]=((-(flow*c*Tprevious[1])+(flow*c*Tprevious[0])-(Qloss*(Tprevious[1]-Tenv)))*(dt/(m*c)))+Tprevious[1]
    Ttry[2]=((-(flow*c*Tprevious[2])+(flow*c*Tprevious[1])-(Qloss*(Tprevious[2]-Tenv)))*(dt/(m*c)))+Tprevious[2]
    Ttry[3]=((-(flow*c*Tprevious[3])+(flow*c*Tprevious[2])-(Qloss*(Tprevious[3]-Tenv)))*(dt/(m*c)))+Tprevious[3]
    Ttry[4]=((-(flow*c*Tprevious[4])+(flow*c*Tprevious[3])-(Qloss*(Tprevious[4]-Tenv)))*(dt/(m*c)))+Tprevious[4]
    Ttry[5]=((-(flow*c*Tprevious[5])+(flow*c*Tprevious[4])-(Qloss*(Tprevious[5]-Tenv)))*(dt/(m*c)))+Tprevious[5]
    Ttry[6]=((-(flow*c*Tprevious[6])+(flow*c*Tprevious[5])-(Qloss*(Tprevious[6]-Tenv)))*(dt/(m*c)))+Tprevious[6]
    Ttry[7]=((-(flow*c*Tprevious[7])+(flow*c*Tprevious[6])-(Qloss*(Tprevious[7]-Tenv)))*(dt/(m*c)))+Tprevious[7]
    Ttry[8]=((-(flow*c*Tprevious[8])+(flow*c*Tprevious[7])-(Qloss*(Tprevious[8]-Tenv)))*(dt/(m*c)))+Tprevious[8]
    Ttry[9]=((-(flow*c*Tprevious[9])+(flow*c*Tprevious[8])-(Qloss*(Tprevious[9]-Tenv)))*(dt/(m*c)))+Tprevious[9]
    THPreturn =Ttry[nseg-1]
    return Ttry,THPreturn 
"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def dTES_singlestep(Tloadreturn,Tprevious,m,cp,tstep,flow,Qloss,Troom,TESbnds,nseg):
    Ttry=[0]*10
    Ttry[0]=((-(flow*cp*Tprevious[0])+(flow*cp*Tprevious[1])-(Qloss*(Tprevious[0]-Troom)))*(tstep/(m*cp)))+Tprevious[0]
    Ttry[1]=((-(flow*cp*Tprevious[1])+(flow*cp*Tprevious[2])-(Qloss*(Tprevious[1]-Troom)))*(tstep/(m*cp)))+Tprevious[1]
    Ttry[2]=((-(flow*cp*Tprevious[2])+(flow*cp*Tprevious[3])-(Qloss*(Tprevious[2]-Troom)))*(tstep/(m*cp)))+Tprevious[2]
    Ttry[3]=((-(flow*cp*Tprevious[3])+(flow*cp*Tprevious[4])-(Qloss*(Tprevious[3]-Troom)))*(tstep/(m*cp)))+Tprevious[3]
    Ttry[4]=((-(flow*cp*Tprevious[4])+(flow*cp*Tprevious[5])-(Qloss*(Tprevious[4]-Troom)))*(tstep/(m*cp)))+Tprevious[4]
    Ttry[5]=((-(flow*cp*Tprevious[5])+(flow*cp*Tprevious[6])-(Qloss*(Tprevious[5]-Troom)))*(tstep/(m*cp)))+Tprevious[5]
    Ttry[6]=((-(flow*cp*Tprevious[6])+(flow*cp*Tprevious[7])-(Qloss*(Tprevious[6]-Troom)))*(tstep/(m*cp)))+Tprevious[6]
    Ttry[7]=((-(flow*cp*Tprevious[7])+(flow*cp*Tprevious[8])-(Qloss*(Tprevious[7]-Troom)))*(tstep/(m*cp)))+Tprevious[7]
    Ttry[8]=((-(flow*cp*Tprevious[8])+(flow*cp*Tprevious[9])-(Qloss*(Tprevious[8]-Troom)))*(tstep/(m*cp)))+Tprevious[8]
    Ttry[9]=((-(flow*cp*Tprevious[9])+(flow*cp*Tloadreturn)-(Qloss*(Tprevious[9]-Troom)))*(tstep/(m*cp)))+Tprevious[9]
    Tloadin=Ttry[0]
    return Ttry,Tloadin 