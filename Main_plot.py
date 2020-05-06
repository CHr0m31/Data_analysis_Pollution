"""
Name: request for which data to plot

what the programme does: get the functions from Plotting functions
                         get the user's input
                         use the user's input and put into the correct function 
                         graph of different time frame will be plot according to what the user requested
                         ask the user if he wants to repeat the programme but using different function
                         if yes: repeat the programme
                         else: close the programme

"""
import Time_Frame
see = 'yes'

while see.lower() not in ('no','n'):
    print('Which data do you want to plot? SO2 or PM10')
    
    x = input()
    
    while x.upper() not in ('SO2','PM10','all'):
        print('Please input again')
        print('Which data do you want to plot? SO2 or PM10')
        x = input()
    print('Which area do you want to see? Central,North,South,East,West,all')
    
    area = input()
    
    while area.lower() not in ('central','north','south','east','west','all'):
        print('Area not found')
        print('Which area do you want to see? Central,North,South,East,West,all')
        area = input()
    print('Do you want your plot to be presented in monthly or yearly?'
          '\nD for daily,W for weekly, M for monthly, Y for yearly')
    
    frame = input()
   
    while frame.lower() not in ('daily','d','weekly','w','monthly','m','yearly','y'):
        print('Please input again')
        print('Do you want your plot to be presented in monthly or yearly? \nW for weekly, M for monthly, Y for yearly')
        frame = input()
    print('\n')
    
    if frame.lower() == 'y' or frame.lower() == 'yearly':  
        Time_Frame.data_conversion(x.upper())
        Time_Frame.Create_Yearly(area.lower())

        
    elif frame.lower() == 'm' or frame.lower() == 'monthly':
        Time_Frame.data_conversion(x.upper())
        Time_Frame.Create_Monthly(area.lower())
        
    elif frame.lower() == 'w' or frame.lower() == 'weekly':
        Time_Frame.data_conversion(x.upper())        
        Time_Frame.Create_Weekly(area.lower())
    
    elif frame.lower() == 'd' or frame.lower() == 'daily':
        Time_Frame.data_conversion(x.upper())
        Time_Frame.Create_Daily(area.lower())  
        
    print('Do you want to see other graph? Yes or No')
    see = input()


    