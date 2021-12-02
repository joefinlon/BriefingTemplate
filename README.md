# BriefingTemplate
Generates a PowerPoint forecast briefing template for the IMPACTS project.

## Usage
1. Modify one of the provided namelists, or make a copy with a different filename.  
2. Execute the following command in a terminal window: ```python briefing.py [namelist].txt```

## Modifying the Namelist
- *presentationPath:* directory where graphics will be downloaded  
- *presentationType:* type of briefing to create (morning, evening)  
- *presentationHour:* 2-digit UTC hour when the briefing will be given  
- *modelList:* 'default' or list of 1+ models to use (comma-separated)  
- *initializeTime:* 'now' or time [YYYYMMDDHH] of start of the Day 0 period  
- *region:* 'usne', 'usmw'  
- *crossSection:* orientation of SBU-WRF model cross sections centered on LI ('n-s', 'nw-se', 'w-e', 'sw-ne)  
- *showWeather:* make slides showing the past and current weather ('True', 'False')  
- *showShortTerm:* make slides showing the Day 0-2 and detailed forecast ('True', 'False')  
- *showDetailed:* make slides showing Day 0-1 hourly graphics ('True', 'False')  
- *showLongTerm:* make slides showing the long-range forecast ('True', 'False')  
- *briefingUpdate:* save the presentation as a new filename ('True', 'False')