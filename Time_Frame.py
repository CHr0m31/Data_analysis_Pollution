'''
Name: Plotting functions

what the programme does:Read the data in excel database
                        Change the data into dataframe
                        
            in daily: the programme will check for the number of days since the start of the collection(self input)
                      plot the graph according to 24hours
                      check the mean of each region
                      check the max of each region
                      check the mean of all the regions
                      input the mean and max value into the graph
                      
                      
            in weekly: The programme will check the start of collection
                       check when is the start of each week and the date in that week
                       plot the graph according to the weeks
                       check the mean of each region
                       check the max of each region
                       check the mean of all the regions
                       input the mean and max value into the graph
                       
            in monthly: The programme will check the start of collection
                        Check the number of days in each month 
                        input that amount of data into each month
                        plot the graph according to each month
                        check the mean of each region
                        check the max of each region
                        check the mean of all the regions
                        input the mean and max value into the graph                        
                        
            in yearly:  The programme will check the start of collection
                        check the number of days to the end of the year
                        input the data into that year 
                        if there are more data that is not used, it will be put into the following year
                        plot the graph according to each year
                        check the mean of each region
                        check the max of each region
                        check the mean of all the regions
                        input the mean and max value into the graph                        
'''
import pandas as pd 
from openpyxl import load_workbook 
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
import os

dirpath = os.path.dirname(os.path.realpath(__file__))

class Create_Daily():
    def __init__(self,area):
        from time import strftime
        from datetime import timedelta , datetime
        today = datetime.today().strftime('%Y-%m-%d')
        
        

        if strftime("%H") < '17':
            date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        
        else:
            date = today
        todaytime = str(date) + ' 17:00:00'
        
        import datetime
        begin = '2019-09-16 18:00:00'
        one_day = datetime.timedelta(1)
        end = todaytime  
        dt_start = datetime.datetime.strptime(begin, '%Y-%m-%d %H:%M:%S')
        dt_end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        
        self.start_dates = [dt_start]
        self.end_dates = []
        today = dt_start
        daily_name = []
        daily_name.append(today.strftime('%Y-%m-%d'))
        while today <= dt_end:
            #print(today)
            tomorrow = today + one_day
            self.start_dates.append(tomorrow)
            tomorrow = tomorrow - timedelta(hours=1)
            self.end_dates.append(tomorrow)
            daily_name.append(tomorrow.strftime('%Y-%m-%d'))
            today = tomorrow + timedelta(hours=1)
        
        self.end_dates.append(dt_end + one_day)
        startD = 0
        x = 0
        #checking the start date and end date 
#        print(self.start_dates , '\n', self.end_dates)        
        for days in daily_name:

            #check if the folder contains the file, if it does, it will skip the plot
            
            if name_wanted == 'SO2':
                pollutant_name = 'SO2'
            elif name_wanted == 'PM10':
                pollutant_name = 'PM10'
            plot_name = pollutant_name+'_'+days+'.png' 
            
            if area == 'central':                    
                Path_area = '/Central/Daily/'
                
            elif area == 'north':
                Path_area = '/North/Daily/'
                
            elif area == 'south':
                Path_area = '/South/Daily/'
                   
            elif area == 'east':
                Path_area = '/East/Daily/'
                
            elif area == 'west':
                Path_area = '/West/Daily/'
                
            elif area == 'all':
                Path_area = '/All/Daily/'
                                
            Path_dir = dirpath+'/'+pollutant_name+Path_area    
            Path = Path_dir+plot_name
            if os.path.isfile(Path) == True:
                continue      
                
            print(days)
                
            endD = startD + 24 

            n = data_created[startD:endD]
            startD = endD 
            
            #Checking the date when the program runs 
            time = pd.date_range(start = self.start_dates[x], end =self.end_dates[x], freq = 'H')    
            time2 = pd.date_range(start = self.start_dates[x], end =self.end_dates[x], freq = 'H')
          
            #Statistic for central data
            
            Central = n.loc[:,'Central']
            average_central_hour = np.nanmean(Central)
            max_central= np.nanmax(Central)
            min_central = np.nanmin(Central)
            sum_central = np.nansum(Central)
            
            #Statistic for South data
            South = n.loc[:,'South']
            average_south_hour = np.nanmean(South)
            max_south= np.nanmax(South)
            min_south = np.nanmin(South)
            sum_south = np.nansum(South)
            
            #Statistic for North data
            North = n.loc[:,'North']
            average_north_hour = np.nanmean(North)
            max_north= np.nanmax(North)
            min_north = np.nanmin(North)
            sum_north = np.nansum(North)
                        
            #Statistic for West data         
            West = n.loc[:,'West']
            average_west_hour = np.nanmean(West)
            max_west= np.nanmax(West)
            min_west = np.nanmin(West)
            sum_west = np.nansum(West)
            
            
            #Statistic for East data           
            East = n.loc[:,'East']
            average_east_hour = np.nanmean(East)
            max_east= np.nanmax(East)
            min_east = np.nanmin(East)
            sum_east = np.nansum(East)
            
             
            #Statistic for overall data
            overall = [min_east,min_west,min_north,min_south,min_central,
                       max_east,max_west,max_north,max_south,max_central]
            sum_overall = sum_east + sum_west + sum_north + sum_south + sum_central           
            average_overall_hour = sum_overall/(5*len(time))
            
            max_overall= np.nanmax(overall)
#            min_overall = np.nanmin(overall)

            
            #plotting of graph
            plt.figure()
            ax = plt.gca()
            
            if area == 'central':
                plt.plot(time, n['Central'], '-m', label = 'Central',linewidth=2.0)
                ax.annotate('Central Max ='+str(max_central), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('Central min ='+str(min_central), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('Central Average = {:.3f}'.format(average_central_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                if name_wanted == 'SO2':
                    plt.ylim([0,max_central+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_central+30])
                    
                    
            elif area == 'north':
                plt.plot(time, n['North'], '-b', label = 'North',linewidth=2.0)
                ax.annotate('North Max ='+str(max_north), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('North Min ='+str(min_north), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('North Average = {:.3f}'.format(average_north_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                if name_wanted == 'SO2':
                    plt.ylim([0,max_north+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_north+30])



            elif area == 'south':
                ax.annotate('South Max ='+str(max_south), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('South Min ='+str(min_south), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('South Average = {:.3f}'.format(average_south_hour), xy=(75,220),fontsize= 10,xycoords='figure points')

                plt.plot(time, n['South'], '-g', label = 'South',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_south+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_south+30])

                    
            elif area == 'east':
                ax.annotate('East Max ='+str(max_east), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('East Min ='+str(min_east), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('East Average = {:.3f}'.format(average_east_hour), xy=(75,220),fontsize= 10,xycoords='figure points')

                plt.plot(time, n['East'], '-r', label = 'East',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_east+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_east+30])



            elif area == 'west':
                ax.annotate('West Max ='+str(max_west), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('West Min ='+str(min_west), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('West Average = {:.3f}'.format(average_west_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                
                plt.plot(time, n['West'], '-c', label = 'West',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_west+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_west+30])


            elif area == 'all':
                ax.annotate('Central Max ='+str(max_central), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('North Max ='+str(max_north), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('South Max ='+str(max_south), xy=(75,220),fontsize= 10,xycoords='figure points')
                ax.annotate('East Max ='+str(max_east), xy=(75,210),fontsize= 10,xycoords='figure points')
                ax.annotate('West Max ='+str(max_west), xy=(75,200),fontsize= 10,xycoords='figure points')                
                ax.annotate('Overall Max ='+str(max_overall), xy=(180,240),fontsize= 10,xycoords='figure points')
#                ax.annotate('Overall Min ='+str(min_overall), xy=(180,230),fontsize= 10,xycoords='figure points')
                ax.annotate('Average of all area \n= {:.3f}'.format(average_overall_hour), xy=(180,210),fontsize= 10,xycoords='figure points')

                if name_wanted == 'SO2':
                    plt.ylim([0,max_overall+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_overall+30])


                plt.plot(time, n['Central'], '-m', label = 'Central',linewidth=2.0)
                plt.plot(time, n['North'], '-b', label = 'North',linewidth=2.0)
                plt.plot(time, n['South'], '-g', label = 'South',linewidth=2.0)
                plt.plot(time, n['East'], '-r', label = 'East',linewidth=2.0)
                plt.plot(time, n['West'], '-c', label = 'West',linewidth=2.0)
            plt.legend(loc = 'upper right',frameon=False)   
            
            plt.xlabel(days)
            plt.xticks(time2, fontsize = 10, rotation = 45)

            ax.xaxis.set_major_formatter(DateFormatter("%H"))
            if name_wanted == 'SO2':

                plt.ylabel('Daily Sulphur Dioxide (µg/m3)')
                
            elif name_wanted == 'PM10':
                plt.ylabel('Daily PM10 (µg/m3)')

            

   
            plt.savefig(Path)
            plt.show()
            print('\n')
            #plt.close()
            x = x + 1
                        
        print('Graph has been saved in the saved folder: \n' , Path_dir)                
class Create_Weekly():
    def __init__(self,area):
        from time import strftime
        from datetime import timedelta , datetime
        today = datetime.today().strftime('%Y-%m-%d')
        
        

        if strftime("%H") < '17':
            date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        
        else:
            date = today
        todaytime = str(date) + ' 17:00:00'
              
        import datetime
        begin = '2019-09-15 18:00:00'
        end = todaytime
            
        dt_start = datetime.datetime.strptime(begin, '%Y-%m-%d %H:%M:%S')
        dt_end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        one_day = datetime.timedelta(1)
        self.start_dates = [dt_start]
        self.end_dates = []
        today = dt_start
        week_name = []
        week_name.append(today.strftime('%Y-%m-%d'))
        while today <= dt_end:
            #print(today)
            tomorrow = today + one_day
            if tomorrow.isocalendar()[1] != today.isocalendar()[1]:
                self.start_dates.append(tomorrow)
                tomorrow = tomorrow - timedelta(hours=1)
                self.end_dates.append(tomorrow)
                tomorrow += timedelta(hours=1)
                week_name.append(tomorrow.strftime('%Y-%m-%d'))
            today = tomorrow 
        
        self.end_dates.append(dt_end)
        week_days = []   
        for i in range(len(self.end_dates)):
            delta = self.end_dates[i] - self.start_dates[i]
            week_days.append(delta.days)
        start = 0
        x = 0
        
#        checking the start date and end date 
#        print(self.start_dates , '\n', self.end_dates)
        for week in week_name:


            end = start + (week_days[x]+1) * 24 

            n = data_created[start:end]

            
            if name_wanted == 'SO2':
                pollutant_name = 'SO2'
            elif name_wanted == 'PM10':
                pollutant_name = 'PM10'
#            plot_name_next = pollutant_name+'_'+week_name[x+1]+'.png' 
#            print(plot_name_next)
            
            if area == 'central':                    
                Path_area = '/Central/Weekly/'
                
            elif area == 'north':
                Path_area = '/North/Weekly/'
                
            elif area == 'south':
                Path_area = '/South/Weekly/'
                   
            elif area == 'east':
                Path_area = '/East/Weekly/'
                
            elif area == 'west':
                Path_area = '/West/Weekly/'
                
            elif area == 'all':
                Path_area = '/All/Weekly/'
                                
        
#            Path = dirpath+'/'+pollutant_name+Path_area+plot_name_next
#            if os.path.isfile(Path) == True:
#                continue
 
            
            
            start = end
            print(week)
            #Checking the date when the program runs 
            time = pd.date_range(start = self.start_dates[x], end =self.end_dates[x], freq = 'H')    
            time2 = pd.date_range(start = self.start_dates[x], end =self.end_dates[x], freq = '1D')

            #Statistic for central data
            
            Central = n.loc[:,'Central']
            average_central_hour = np.nanmean(Central)
            max_central= np.nanmax(Central)
            min_central = np.nanmin(Central)
            sum_central = np.nansum(Central)
            
            #Statistic for South data
            South = n.loc[:,'South']
            average_south_hour = np.nanmean(South)
            max_south= np.nanmax(South)
            min_south = np.nanmin(South)
            sum_south = np.nansum(South)
            
            #Statistic for North data
            North = n.loc[:,'North']
            average_north_hour = np.nanmean(North)
            max_north= np.nanmax(North)
            min_north = np.nanmin(North)
            sum_north = np.nansum(North)
                        
            #Statistic for West data         
            West = n.loc[:,'West']
            average_west_hour = np.nanmean(West)
            max_west= np.nanmax(West)
            min_west = np.nanmin(West)
            sum_west = np.nansum(West)
            
            
            #Statistic for East data           
            East = n.loc[:,'East']
            average_east_hour = np.nanmean(East)
            max_east= np.nanmax(East)
            min_east = np.nanmin(East)
            sum_east = np.nansum(East)
            
             
            #Statistic for overall data
            overall = [min_east,min_west,min_north,min_south,min_central,
                       max_east,max_west,max_north,max_south,max_central]
            sum_overall = sum_east + sum_west + sum_north + sum_south + sum_central           
            average_overall_hour = sum_overall/(5*len(time))
            
            max_overall= np.nanmax(overall)
#            min_overall = np.nanmin(overall)

            
            #plotting of graph
            plt.figure()
            ax = plt.gca()
            
            if area == 'central':
                plt.plot(time, n['Central'], '-m', label = 'Central',linewidth=2.0)
                ax.annotate('Central Max ='+str(max_central), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('Central min ='+str(min_central), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('Central Average = {:.3f}'.format(average_central_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                if name_wanted == 'SO2':
                    plt.ylim([0,max_central+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_central+30])
                    
                  
                    
            elif area == 'north':
                plt.plot(time, n['North'], '-b', label = 'North',linewidth=2.0)
                ax.annotate('North Max ='+str(max_north), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('North Min ='+str(min_north), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('North Average = {:.3f}'.format(average_north_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                if name_wanted == 'SO2':
                    plt.ylim([0,max_north+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_north+30])



            elif area == 'south':
                ax.annotate('South Max ='+str(max_south), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('South Min ='+str(min_south), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('South Average = {:.3f}'.format(average_south_hour), xy=(75,220),fontsize= 10,xycoords='figure points')

                plt.plot(time, n['South'], '-g', label = 'South',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_south+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_south+30])
                    
                    
            elif area == 'east':
                ax.annotate('East Max ='+str(max_east), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('East Min ='+str(min_east), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('East Average = {:.3f}'.format(average_east_hour), xy=(75,220),fontsize= 10,xycoords='figure points')

                plt.plot(time, n['East'], '-r', label = 'East',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_east+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_east+30])


            elif area == 'west':
                ax.annotate('West Max ='+str(max_west), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('West Min ='+str(min_west), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('West Average = {:.3f}'.format(average_west_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                
                plt.plot(time, n['West'], '-c', label = 'West',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_west+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_west+30])


            elif area == 'all':
                ax.annotate('Central Max ='+str(max_central), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('North Max ='+str(max_north), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('South Max ='+str(max_south), xy=(75,220),fontsize= 10,xycoords='figure points')
                ax.annotate('East Max ='+str(max_east), xy=(75,210),fontsize= 10,xycoords='figure points')
                ax.annotate('West Max ='+str(max_west), xy=(75,200),fontsize= 10,xycoords='figure points')                
                ax.annotate('Overall Max ='+str(max_overall), xy=(180,240),fontsize= 10,xycoords='figure points')
#                ax.annotate('Overall Min ='+str(min_overall), xy=(180,230),fontsize= 10,xycoords='figure points')
                ax.annotate('Average of all area \n= {:.3f}'.format(average_overall_hour), xy=(180,210),fontsize= 10,xycoords='figure points')
               
                if name_wanted == 'SO2':
                    plt.ylim([0,max_overall+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_overall+30])
                    
                plt.plot(time, n['Central'], '-m', label = 'Central',linewidth=2.0)
                plt.plot(time, n['North'], '-b', label = 'North',linewidth=2.0)
                plt.plot(time, n['South'], '-g', label = 'South',linewidth=2.0)
                plt.plot(time, n['East'], '-r', label = 'East',linewidth=2.0)
                plt.plot(time, n['West'], '-c', label = 'West',linewidth=2.0)
            plt.legend(loc = 'upper right',frameon=False)   
            
            plt.xlabel('Date')
            plt.xticks(time2, fontsize = 10, rotation = 45)

            ax.xaxis.set_major_formatter(DateFormatter("%m/%d"))
            if name_wanted == 'SO2':
                plt.ylabel('Weekly Sulphur Dioxide (µg/m3)')
                
            elif name_wanted == 'PM10':
                plt.ylabel('Weekly PM10 (µg/m3)')
            
            #best placement for graph

            plot_name = pollutant_name+'_'+week+'.png'
            Path_dir = dirpath+'/'+pollutant_name+Path_area
            Path = Path_dir+plot_name
            plt.savefig(Path)
            plt.show()
            print('\n')
            #plt.close()
            x = x + 1
            
        print('Graph has been saved in the saved folder: \n' , Path_dir)            

class Create_Monthly():
    def __init__(self,area):
        from time import strftime
        from datetime import timedelta , datetime
        today = datetime.today().strftime('%Y-%m-%d')
        
        

        if strftime("%H") < '17':
            date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        
        else:
            date = today
        todaytime = str(date) + ' 17:00:00'
        
        begin = '2019-09-15 18:00:00'
        end = todaytime
        given_date = datetime.today().date()
        first_day_of_month = given_date.replace(day=1) 
        import datetime    
        dt_start = datetime.datetime.strptime(begin, '%Y-%m-%d %H:%M:%S')
        dt_end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        one_day = datetime.timedelta(1)
        self.start_dates = [dt_start]
        self.end_dates = []
        today = dt_start
        month_name = []
        month_name.append(today.strftime('%B_%Y'))
        while today <= dt_end:
            #print(today)
            tomorrow = today + one_day
            if tomorrow.month != today.month:
                if first_day_of_month != date:
                    if given_date.month != tomorrow.month:
                        self.start_dates.append(tomorrow)
                        tomorrow = tomorrow - timedelta(hours=1)
                        self.end_dates.append(tomorrow)
                        tomorrow += timedelta(hours=1)
                        month_name.append(tomorrow.strftime('%B %Y'))

            today = tomorrow
        
        self.end_dates.append(dt_end)
        month_days = []   
        for i in range(len(self.end_dates)):
            delta = self.end_dates[i] - self.start_dates[i]
            month_days.append(delta.days)
        start = 0
        x = 0
#        #checking the start date and end date 
#        print(self.start_dates , '\n', self.end_dates)        

        
        for month in month_name:

            print(month)
            
            end = start + (month_days[x]+1) * 24    
            n = data_created[start:end]
            start = end
  
            
            
            #Creating the time interval for plotting and checking  
            time = pd.date_range(start = self.start_dates[x], end =self.end_dates[x], freq = 'H')
            
            time2 = pd.date_range(start = self.start_dates[x], end =self.end_dates[x], freq = '3D')
            #Creating the statistic for the graph
            
            #Statistic for central data
            
            Central = n.loc[:,'Central']
            average_central_hour = np.nanmean(Central)
            max_central= np.nanmax(Central)
            min_central = np.nanmin(Central)
            sum_central = np.nansum(Central)
            
            #Statistic for South data
            South = n.loc[:,'South']
            average_south_hour = np.nanmean(South)
            max_south= np.nanmax(South)
            min_south = np.nanmin(South)
            sum_south = np.nansum(South)
            
            #Statistic for North data
            North = n.loc[:,'North']
            average_north_hour = np.nanmean(North)
            max_north= np.nanmax(North)
            min_north = np.nanmin(North)
            sum_north = np.nansum(North)
                        
            #Statistic for West data         
            West = n.loc[:,'West']
            average_west_hour = np.nanmean(West)
            max_west= np.nanmax(West)
            min_west = np.nanmin(West)
            sum_west = np.nansum(West)
            
            
            #Statistic for East data           
            East = n.loc[:,'East']
            average_east_hour = np.nanmean(East)
            max_east= np.nanmax(East)
            min_east = np.nanmin(East)
            sum_east = np.nansum(East)
            
             
            #Statistic for overall data
            overall = [min_east,min_west,min_north,min_south,min_central,
                       max_east,max_west,max_north,max_south,max_central]
            sum_overall = sum_east + sum_west + sum_north + sum_south + sum_central
            average_overall_hour = sum_overall/(5*len(time))
            
            max_overall= np.nanmax(overall)
#            min_overall = np.nanmin(overall)

            
            #plotting of graph
            
            plt.figure()
            ax = plt.gca()
            
            if area == 'central':
                plt.plot(time, n['Central'], '-m', label = 'Central',linewidth=2.0)
                ax.annotate('Central Max ='+str(max_central), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('Central min ='+str(min_central), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('Central Average = {:.3f}'.format(average_central_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                if name_wanted == 'SO2':
                    plt.ylim([0,max_central+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_central+30])

                #creating path for the plot
                Path_area = '/Central/Monthly/'

            elif area == 'north':
                plt.plot(time, n['North'], '-b', label = 'North',linewidth=2.0)
                ax.annotate('North Max ='+str(max_north), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('North Min ='+str(min_north), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('North Average = {:.3f}'.format(average_north_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                if name_wanted == 'SO2':
                    plt.ylim([0,max_north+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_north+30])

                #creating path for the plot
                Path_area = '/North/Monthly/'

            elif area == 'south':
                ax.annotate('South Max ='+str(max_south), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('South Min ='+str(min_south), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('South Average = {:.3f}'.format(average_south_hour), xy=(75,220),fontsize= 10,xycoords='figure points')

                plt.plot(time, n['South'], '-g', label = 'South',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_south+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_south+30])

                #creating path for the plot
                Path_area = '/South/Monthly/'
            elif area == 'east':
                ax.annotate('East Max ='+str(max_east), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('East Min ='+str(min_east), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('East Average = {:.3f}'.format(average_east_hour), xy=(75,220),fontsize= 10,xycoords='figure points')

                plt.plot(time, n['East'], '-r', label = 'East',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_east+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_east+30])
                
                
                #creating path for the plot
                Path_area = '/East/Monthly/'
                
            elif area == 'west':
                ax.annotate('West Max ='+str(max_west), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('West Min ='+str(min_west), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('West Average = {:.3f}'.format(average_west_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                
                plt.plot(time, n['West'], '-c', label = 'West',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_west+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_west+30])
                
                #creating path for the plot
                Path_area = '/West/Monthly/'
            elif area == 'all':
                ax.annotate('Central Max ='+str(max_central), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('North Max ='+str(max_north), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('South Max ='+str(max_south), xy=(75,220),fontsize= 10,xycoords='figure points')
                ax.annotate('East Max ='+str(max_east), xy=(75,210),fontsize= 10,xycoords='figure points')
                ax.annotate('West Max ='+str(max_west), xy=(75,200),fontsize= 10,xycoords='figure points')                
                ax.annotate('Overall Max ='+str(max_overall), xy=(180,240),fontsize= 10,xycoords='figure points')
#                ax.annotate('Overall Min ='+str(min_overall), xy=(180,230),fontsize= 10,xycoords='figure points')
                ax.annotate('Average of all area \n= {:.3f}'.format(average_overall_hour), xy=(180,210),fontsize= 10,xycoords='figure points')

                if name_wanted == 'SO2':
                    plt.ylim([0,max_overall+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_overall+30])
                
                #creating path for the plot
                Path_area = '/All/Monthly/'
                plt.plot(time, n['Central'], '-m', label = 'Central',linewidth=2.0)
                plt.plot(time, n['North'], '-b', label = 'North',linewidth=2.0)
                plt.plot(time, n['South'], '-g', label = 'South',linewidth=2.0)
                plt.plot(time, n['East'], '-r', label = 'East',linewidth=2.0)
                plt.plot(time, n['West'], '-c', label = 'West',linewidth=2.0)
            plt.legend(loc = 'upper right',frameon=False)
#           plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)    
            plt.xlabel('Date')
            plt.xticks(time2, fontsize = 10, rotation = 45)
            
            ax.xaxis.set_major_formatter(DateFormatter("%m/%d"))
            if name_wanted == 'SO2':
                pollutant_name = 'SO2'
                plt.ylabel('Monthly Sulphur Dioxide (µg/m3)')
            elif name_wanted == 'PM10':
                plt.ylabel('Monthly PM10 (µg/m3)')
                pollutant_name = 'PM10'
            
            
            
            #best placement for graph
            
            plot_name = pollutant_name+'_'+month+'.png' 
            Path_dir = dirpath+'/'+pollutant_name+Path_area
            Path = Path_dir+plot_name
            plt.savefig(Path)
            plt.show()
            print('\n')
            #plt.close()
            x = x + 1

        print('Graph has been saved in the saved folder: \n' , Path_dir)

        
class Create_Yearly():
    def __init__(self,area):
        from time import strftime
        from datetime import timedelta , datetime
        today = datetime.today().strftime('%Y-%m-%d')
        
        

        if strftime("%H") < '17':
            date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        
        else:
            date = today
        todaytime = str(date) + ' 17:00:00'
              
        import datetime
        begin = '2019-09-15 18:00:00'
        end = todaytime
            
        dt_start = datetime.datetime.strptime(begin, '%Y-%m-%d %H:%M:%S')
        dt_end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        one_day = datetime.timedelta(1)
        self.start_dates = [dt_start]
        self.end_dates = []
        today = dt_start
        year_name = []
        year_name.append(today.strftime('%Y'))
        while today <= dt_end:
            #print(today)
            tomorrow = today + one_day
            if tomorrow.year != today.year:
                self.start_dates.append(tomorrow)
                tomorrow = tomorrow - timedelta(hours=1)
                self.end_dates.append(tomorrow)
                tomorrow += timedelta(hours=1)
                year_name.append(tomorrow.strftime('%Y'))
            today = tomorrow
        
        self.end_dates.append(dt_end)
        year_days = []   
        for i in range(len(self.end_dates)):
            delta = self.end_dates[i] - self.start_dates[i]
            year_days.append(delta.days)
        time = pd.date_range(start = '2019-09-16 18:00:00', end =todaytime, freq = 'H')   
        time2 = pd.date_range(start = '2019-09-16 18:00:00', end =todaytime, freq = '10D')
        start = 0
        x = 0
        
        for n in year_name:
            year = str(n)
            print(year)

            end = start + (year_days[x]+1) * 24 
            n = data_created[start:end]
            start = end
            
            #Checking the date when the program runs 
            time = pd.date_range(start = self.start_dates[x], end =self.end_dates[x], freq = 'H')    
            time2 = pd.date_range(start = self.start_dates[x], end =self.end_dates[x], freq = '2W')

            #Statistic for central data
            
            Central = n.loc[:,'Central']
            average_central_hour = np.nanmean(Central)
            max_central= np.nanmax(Central)
            min_central = np.nanmin(Central)
            sum_central = np.nansum(Central)
            
            #Statistic for South data
            South = n.loc[:,'South']
            average_south_hour = np.nanmean(South)
            max_south= np.nanmax(South)
            min_south = np.nanmin(South)
            sum_south = np.nansum(South)
            
            #Statistic for North data
            North = n.loc[:,'North']
            average_north_hour = np.nanmean(North)
            max_north= np.nanmax(North)
            min_north = np.nanmin(North)
            sum_north = np.nansum(North)
                        
            #Statistic for West data         
            West = n.loc[:,'West']
            average_west_hour = np.nanmean(West)
            max_west= np.nanmax(West)
            min_west = np.nanmin(West)
            sum_west = np.nansum(West)
            
            
            #Statistic for East data           
            East = n.loc[:,'East']
            average_east_hour = np.nanmean(East)
            max_east= np.nanmax(East)
            min_east = np.nanmin(East)
            sum_east = np.nansum(East)
            
             
            #Statistic for overall data
            overall = [min_east,min_west,min_north,min_south,min_central,
                       max_east,max_west,max_north,max_south,max_central]
            sum_overall = sum_east + sum_west + sum_north + sum_south + sum_central           
            average_overall_hour = sum_overall/(5*len(time))
            
            max_overall= np.nanmax(overall)
#            min_overall = np.nanmin(overall)

            
            #plotting of graph
            plt.figure()
            ax = plt.gca()
            
            if area == 'central':
                plt.plot(time, n['Central'], '-m', label = 'Central',linewidth=2.0)
                ax.annotate('Central Max ='+str(max_central), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('Central min ='+str(min_central), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('Central Average = {:.3f}'.format(average_central_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                if name_wanted == 'SO2':
                    plt.ylim([0,max_central+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_central+30])
                Path_area = '/Central/Yearly/'
            elif area == 'north':
                plt.plot(time, n['North'], '-b', label = 'North',linewidth=2.0)
                ax.annotate('North Max ='+str(max_north), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('North Min ='+str(min_north), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('North Average = {:.3f}'.format(average_north_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                if name_wanted == 'SO2':
                    plt.ylim([0,max_north+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_north+30])
                Path_area = '/North/Yearly/'
            elif area == 'south':
                ax.annotate('South Max ='+str(max_south), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('South Min ='+str(min_south), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('South Average = {:.3f}'.format(average_south_hour), xy=(75,220),fontsize= 10,xycoords='figure points')

                plt.plot(time, n['South'], '-g', label = 'South',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_south+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_south+30])
                Path_area = '/South/Yearly/'
            elif area == 'east':
                ax.annotate('East Max ='+str(max_east), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('East Min ='+str(min_east), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('East Average = {:.3f}'.format(average_east_hour), xy=(75,220),fontsize= 10,xycoords='figure points')

                plt.plot(time, n['East'], '-r', label = 'East',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_east+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_east+30])
                Path_area = '/East/Yearly/'
            elif area == 'west':
                ax.annotate('West Max ='+str(max_west), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('West Min ='+str(min_west), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('West Average = {:.3f}'.format(average_west_hour), xy=(75,220),fontsize= 10,xycoords='figure points')
                
                plt.plot(time, n['West'], '-c', label = 'West',linewidth=2.0)
                if name_wanted == 'SO2':
                    plt.ylim([0,max_west+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_west+30])
                Path_area = '/West/Yearly/'
            elif area == 'all':
                ax.annotate('Central Max ='+str(max_central), xy=(75,240),fontsize= 10,xycoords='figure points')
                ax.annotate('North Max ='+str(max_north), xy=(75,230),fontsize= 10,xycoords='figure points')
                ax.annotate('South Max ='+str(max_south), xy=(75,220),fontsize= 10,xycoords='figure points')
                ax.annotate('East Max ='+str(max_east), xy=(75,210),fontsize= 10,xycoords='figure points')
                ax.annotate('West Max ='+str(max_west), xy=(75,200),fontsize= 10,xycoords='figure points')                
                ax.annotate('Overall Max ='+str(max_overall), xy=(180,240),fontsize= 10,xycoords='figure points')
#                ax.annotate('Overall Min ='+str(min_overall), xy=(180,230),fontsize= 10,xycoords='figure points')
                ax.annotate('Average of all area \n= {:.3f}'.format(average_overall_hour), xy=(180,210),fontsize= 10,xycoords='figure points')

                if name_wanted == 'SO2':
                    plt.ylim([0,max_overall+10])
                elif name_wanted == 'PM10':
                    plt.ylim([0,max_overall+30])
                
                plt.plot(time, n['Central'], '-m', label = 'Central',linewidth=2.0)
                plt.plot(time, n['North'], '-b', label = 'North',linewidth=2.0)
                plt.plot(time, n['South'], '-g', label = 'South',linewidth=2.0)
                plt.plot(time, n['East'], '-r', label = 'East',linewidth=2.0)
                plt.plot(time, n['West'], '-c', label = 'West',linewidth=2.0)
                Path_area = '/All/Yearly/'
            plt.legend(loc = 'upper right',frameon=False)   
            
            plt.xlabel('Date')
            plt.xticks(time2, fontsize = 10, rotation = 45)

            ax.xaxis.set_major_formatter(DateFormatter("%m/%d"))
            if name_wanted == 'SO2':
                pollutant_name = 'SO2'
                plt.ylabel('Yearly Sulphur Dioxide (µg/m3)')
                
            elif name_wanted == 'PM10':
                plt.ylabel('Yearly PM10 (µg/m3)')
                pollutant_name = 'PM10'
            
            #saving the graph

            plot_name = pollutant_name+'_'+year+'.png' 
            Path_dir = dirpath+'/'+pollutant_name+Path_area
            Path = dirpath+'/'+pollutant_name+Path_area+plot_name
            plt.savefig(Path)
            plt.show()
            print('\n')
            #plt.close()
            x = x + 1
            
        print('Graph has been saved in the saved folder: \n' , Path_dir)
            

                     
""" Changing the data type in order to plot """
class data_conversion():
    def __init__(self,name):
        global data_created
        global name_wanted
        name_wanted = name
        self.filexlsx = 'output_'+ str(name) +'.xlsx'
        self.filecsv = 'output_'+ str(name) +'.csv'
        
        # read excel
        db_df = pd.read_excel('database.xlsx',name)
        
        # drop lame rows
        db_df.drop(db_df.columns[13:], axis=1, inplace=True)
        
        # drop lame columns
        db_df = db_df[db_df.isnull().sum(axis=1) == 0]
        
        # drop first column (region/time)
        db_df.drop(db_df.columns[0], axis=1, inplace=True)
        
        # writer
        writer = pd.ExcelWriter(self.filexlsx, engine='openpyxl')
        
        # open workbook
        writer.book = load_workbook(self.filexlsx)
        
        # copy worksheet(s)
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        
        # append region/time column
        region_df = pd.DataFrame({'r': ['Time', 'North','South','East','West', 'Central']})
        region_df.to_excel(writer, index=0, header=0)
        
        # while loop to append
        i = 0
        x=0
        while (i < len(db_df)):
            db_df[i:i+6].to_excel(writer, index=0, header=0, startcol=1+x)
            db_df[i+6:i+12].to_excel(writer, index=0, header=0, startcol=13+x)
            i += 12
            x += 24
        # close excel
        writer.close()
        
        # runs the csv_from_excel function:
        self.csv_from_excel(name)
        
        
        #data = pd.read_csv("testing.csv")
        self.data = pd.read_csv(self.filecsv)
        self.data = self.data.T
        
        keys = list(self.data.columns)
        values = list(self.data.iloc[0])
        dictionary = dict(zip(keys,values))
        
        self.data.rename(columns = dictionary, inplace = True)
        
        self.data.drop(['Time'], inplace = True)
        
        self.data = self.data.loc[:,self.data.columns.notnull()]
        
        def remove_brackets(value):
            if value == '-':
                pass
            else:
                return value.split('(',1)[0]
                
        for i in self.data:
            if i == '-':
                i = '0(0)'
            self.data[i] = pd.to_numeric(self.data[i].apply(remove_brackets))
        data_created = self.data
        
    def csv_from_excel(self,name):
        import xlrd
        import csv
        
        wb = xlrd.open_workbook(self.filexlsx)
        sh = wb.sheet_by_name('Sheet1')
        your_csv_file = open(self.filecsv, 'w')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
    
        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum)) 
            
## To plot every single data collected in daily, weekly, monthly and yearly            
#x = ['PM10','SO2']
#for name in x:
#   data_conversion(name)
#   areas = ['central','north','south','east','west','all']
#   for area in areas:
#       Create_Daily(area)
#       Create_Weekly(area)
#       Create_Monthly(area)
#       Create_Yearly(area)