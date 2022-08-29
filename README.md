# CCB_Flex_Sim
Comfort and Climate Box - Design Energy Flexibility Simulator

CCB_Flex_Sim can be used to estimate the design energy flexibility of a Comfort and Climate Box (CCB).
A CCB is known as the smart combination of a heat pump, energy storage and the necessary control modules.
The main goal is to achieve an estimation of the CCB energy flexibility potential by the calculation of the efficiency of the provided energy flexibility, the average charging time and average discharging time.
Therefore, the method incorporates not only the average forced on-time or forced off-time, but also the rebound effect and system efficiency changes related to the energy flexibility services. 

The main script 'MainScript_AllCases' uses two Excel files ('PerformanceData.xlsx' and 'CCBConfiguration.xlsx') as input.
Both Excel files come along with the simulator package and are foreseen of the necessary documentation to guide the user through the input process.
These two files can be changed by the user to modify the CCB configuration and/or heat pump performance.

To take into account the decreasing efficiency of an electrical back-up heater (BUH) in the heat pump system, two flexibility cycles exist:
- Flex1: only compressor-mode until the compressor switch-off temperature
- Flex2: activation of the back-up heater is allowed. If the heat pump is not equipped with a back-up heater, flexibility cycle Flex2 equals cycle Flex1. 

As the heat pump performance is changing under part-load conditions as well as for changing outdoor conditions, four outdoor temperature levels are used. These temperature levels are -7 °C, 2 °C, 7 °C and 12 °C and denoted as 88, 54, 35 and 15 within the scripts (due to the space heating part load of 88 %, 54 %, 35 % and 15 % at these outdoor temperatures, respectively). These temperatures are derived from the European heat pump standards EN 14511 and EN 14825 and are valid for an average European climate with a design outdoor temperature of -10 °C.

The Excel-file 'PerformanceData.xlsx' is used to provide specifications of the heat pump compressor, by providing the thermal and electrical compressor power.
Four tabs ('HP_Data_12°C', 'HP_Data_7°C', 'HP_Data_2°C' and 'HP_Data_-7°C') are used to include the heat-source temperature dependency of air-source heat pumps.
Depending on the heat pump type, the user should provide:
- for air-source heat pumps: each tab includes the heat pump performance data at a specific heat source temperature, namely 12 °C, 7 °C, 2 °C and -7 °C
- for brine-source heat pumps: all tabs include identical performance data as the brine heat source temperature is assumed fixed at 0 °C
- for water-source heat pumps: all tabs include identical performance data as the water heat source temperature is assumed fixed at 10 °C.

It is assumed that five compressor modulation levels are provided by the user within the tab 'HP_Data_Modulation'.
Please make sure that the entered compressor speeds meet the following requirement: Mod_level1 < Mod_level2 < Mod_level3 < Mod_level4 < Mod_level5.
The compressor speed at Mod_level1 should equal the minimum allowed compressor speed, while Mod_level5 equals the maximum compressor speed.
These five modulation levels only require the heat pump part-load performance data at the maximum compressor supply temperature (which equals Flex1 cycles), which is  denoted by Tcomp3.
In addition to the maximum compressor supply temperature Tcomp3, two temperature levels (Tcomp1 and Tcomp2) at heat pump full-load conditions are required.
Herein, Tcomp1 should be maximum 35 °C and Tcomp1 < Tcomp2 < Tcomp3.

Within the Excel-file 'CCBConfiguration.xlsx', the CCB configuration and general parameters such as the preferred time step and result file folder can be selected.
It is required that the maximum compressor supply temperature Tcomp3 (within 'PerformanceData.xlsx') equals both T_SHmax1 and T_DHWmax1 (within 'CCBConfiguration.xlsx').

After specifying the CCB composition and its general performance characteristics, the script automatically selects the required calculation procedure.
In the current release, the following cases can be simulated:
- Only space heating (SH) service and no back-up heater availability (Script named with Cases_1_4)
- Both space heating and domestic hot water (DHW) service, but without back-up heater availability (Script named with Cases_5_8)
- Both space heating and domestic hot water service, with back-up heater availability. In space heating mode, the back-up heater operates in series with the compressor until the compressor switch-off temperature. In domestic hot water mode, the back-up heater only operates after the compressor switch-off (Script named with Cases_9_12)
- Both space heating and domestic hot water service, with back-up heater availability. The back-up heater only operates after compressor switch-off in both space heating mode and domestic hot water mode (Script named with Cases_13_16).

In future releases, new cases/combinations will be added.

Depending on the user requirements, the simulation output is provided:
- by Key Performance Indicators (KPI) of the CCB energy flexibility potential on the Python output window
- by Key Performance Indicators (KPI) of the CCB energy flexibility potential in a txt result file named 'Case < User-defined case follow-up number > _Result.txt'
- detailed analysis of the charging process of each flexibility cycle [Flex1 (no_BUH) and Flex2 (with_BUH)], for each outdoor temperature [-7 °C (88), 2 °C (54), 7 °C (35) and 12 °C (15)] and for each service [Space heating (SH) and Domestic hot water (DHW)] in several txt result files named 'Case < User-defined case follow-up number > _Charge_... .txt'


Independent from the chosen output type, each output is foreseen of a description with their respective units.

During the calculation process, the tool uses several charging and discharging cycles. 
Firstly, all charging phases are calculated and the average thermal energy storage temperature at the end of the charging phase is used as input for the discharging phase in a second step.
Hence, the charging and discharging phases are coupled to assure equal state-of-charge values of the thermal energy storages.
The user will receive a notification when the thermal energy storage will not be fully charged due to heat pump safety constraints.
Such a notification message occurs when the heat pump supply temperature reaches values five degrees above its temperature setpoint.
In those cases, the charging phase will stop before the storage is fully charged, while the discharging phase will also start from this lower temperature to keep equal state-of-charge conditions. 
When charging cycles are performed without reaching errors, the output window will print 'SUCCESSFUL' for each cycle iteration.

# Release history
- April 2022: release v1.0

# Support
The goal of providing this simulation tool is to allow users to estimate the energy flexibility potential of a Comfort and Climate Box within Python. 
Our tool was initially developed in Python 3.9.
If you have found a bug, a suggestion for improvement or a new case/configuration that you want to test, please feel free to take contact or to rise an issue.

# References
Maarten Evens - maarten.evens@kuleuven.be

Alice Mugnini - a.mugnini@staff.univpm.it

Alessia Arteconi - a.arteconi@staff.univpm.it

Please cite CCB Flex Sim by using the information below:
@article{EVENS2022119154,
title = {Design energy flexibility characterisation of a heat pump and thermal energy storage in a Comfort and Climate Box},
journal = {Applied Thermal Engineering},
volume = {216},
pages = {119154},
year = {2022},
issn = {1359-4311},
doi = {https://doi.org/10.1016/j.applthermaleng.2022.119154},
author = {Maarten Evens and Alice Mugnini and Alessia Arteconi},
keywords = {Heat pump, Energy flexibility, Flexibility quantification, Demand response, Thermal energy storage, Comfort and climate box},
}
