# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 10:03:59 2014

@author: hxu
"""
"""
it used for getting drifter survive information from erddap based on id_list and time_period ()
Before running this program, ask Huanxin to get drifter id from 'nova' service
After running this program, it could plot a graph of drifter survive. And you could save that by yourself
input values: time period,ids
function uses:getobs_drift_byid, getobs_drift_byrange, haversine,get_coastline_coordinate
output : a plot with average days and total drifters 
"""
import datetime as dt
import sys
import os
import matplotlib.pyplot as plt
import pytz
from pandas import *
#import pandas.tools.rplot as rplot
from matplotlib.dates import date2num
from drifter_functions import getobs_drift_byrange,getobs_drift_byid,get_coastline_coordinate,haversine
ops=os.defpath
pydir='../'
sys.path.append(pydir)
#################Input values#############################################
input_time=[dt.datetime(1980,1,1,0,0,0,0,pytz.UTC),dt.datetime(2015,7,1,0,0,0,0,pytz.UTC)] # start time and end time


ids=[['55291', '    55292', '    55293', '    57202', '    65204', '    65205', '    65206', '    65291', '    65292', '    65293', '    65294', '    65295', '    66207', '    90301', '    90302', '    94303', '    94491', '    94492', '    95491', '    95492', '    97115', ' 97420703', ' 97420704', ' 97420705', ' 97420706', ' 97420707', ' 97420708', ' 97420709', ' 99361212', ' 99420701', ' 99420702', ' 99420703', ' 99420704', ' 99420705', ' 99420706', ' 99420707', ' 99420708', ' 99420709', '100240811', '100361211', '104420701', '1054207019', '1054207020', '105430681', '105430693', '105440671', '105440672', '105440673', '105440674', '105440675', '105440676', '105440681', '1054406810', '1054406811', '1054406812', '1054406813', '105440682', '105440683', '105440684', '105440685', '105440686', '105440687', '105440688', '105440689', '105470641', '105470644', '105470645', '105470646', '106280851', '106280871', '106290881', '106290882', '106290885', '106410702', '106410703', '106410704', '106410706', '106410707', '106410708', '106410709', '106410712', '106420701', '106420702', '106420703', '106420704', '106430691', '106430692', '106430693', '106430701', '106440681', '106440682', '106440683', '107410701', '107410702', '107410703', '107410704', '107410705', '107420701', '1074207010', '1074207011', '1074207012', '107420705', '107420708', '107430691', '107440671', '107440672', '108240811', '108410712', '108430701', '108430702', '1084406710', '1084406711', '109290841', '109290881', '109290885', '109430701', '109430702', '43202', '45380', '453810', '453812', '453813', '453814', '453815', '453816', '453817', '453818', '453819', '45382', '45384', '45386', '45388', '46202', '46382', '46392', '46472', '47202', '47205', '47362', '47382', '47392', '47472', '48202', '48382', '48392', '48472', '49202', '49382', '49392', '49472', '54291', '54292', '55201', '55202', '55203', '55381', '55382', '55383', '55384', '55385', '55386', '56101', '56202', '60301', '60391', '60392', '66201', '66202', '66203', '66204', '66205', '66381', '66382', '66383', '66384', '66385', '66386', '69391', '693910', '693912', '693914', '69393', '69395', '69397', '69399', '70391', '70392', '70395', '70398', '75201', '75202', '75203', '75291', '75292', '75293', '75294', '75295', '75296', '75381', '75382', '75383', '75384', '75385', '75386', '76201', '76202', '76203', '76381', '76382', '76383', '76384', '76385', '76386', '79394', '79395', '79396', '80201', '80301', '80302', '80303', '80304', '80305', '80393', '80394', '80397', '82371', '82372', '82373', '82374', '82375', '82376', '85201', '85202', '85203', '85291', '85292', '85301', '85302', '85303', '85304', '85391', '85392', '85393', '85394', '85395', '85396', '85397', '85398', '85399', '86091', '86301', '87171', '87201', '87301', '87302', '87303', '87304', '88201', '88202', '88461', '88462', '88463', '89301', '89302', '89393', '89394', '89398', '91191', '96101', '96102', '96104', '96105', '96107', '96108', '96111', '96112', '96113', '96114', '96201', '96301', '96302', '96303', '97101', '971010', '97102', '97103', '97104', '97105', '97106', '97107', '97108', '97109', '97111', '97112', '97113', '97114', '97201', '97202', '97301', '97302', '974207010', '974207011', '974207012', '98101', '98102', '98103', '98104', '98105', '98201', '98301', '98302', '99301', '994207010', '994207011', '994207012', '994207013', '994207014', '994207015', '994207016', '994207017', '994207018'] \
,['100420703', '100420704', '107430692', '108250811', '108410831', '108410832', '108410833', '120340752', '120420801', '120420802', '120920371', '124420701', '125420801', '126390731', '126390732', '126390733', '126390734', '127280881', '127280883', '130410701', '130430701', '130430702', '131430701', '133420701', '134400721', '134410691', '134410692', '135410681', '135430701', '136420701', '137410702', '137430661', '137440661', '138430661', '139390721', '139420691']\
,['120410701', '135410701', '136410701', '136410702', '137410701', '139400721', '139420692']\
,['130410703', '130410704', '130410705', '130410708', '138410701']]# id list ,order by Names of Rachel,Eddie,Cassie,Irina,ask Huanxin to modify
'''
ids=[['55291','55292']\
,['100420703', '100420704', '107430692', '108250811', '108410831', '108410832', '108410833', '120340752', '120420801', '120420802', '120920371', '124420701', '125420801', '126390731', '126390732', '126390733', '126390734', '127280881', '127280883', '130410701', '130430701', '130430702', '131430701', '133420701', '134400721', '134410691', '134410692', '135410681', '135430701', '136420701', '137410702', '137430661', '137440661', '138430661', '139390721', '139420691']\
,['120410701', '135410701', '136410701', '136410702', '137410701', '139400721', '139420692']\
,['130410703', '130410704', '130410705', '130410708', '138410701']]
'''
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑Input values↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑#

drifter_name=['Rachel','Eddie','Cassie','Irina']  # names of 4 subplots , they can be changed
fig, axes = plt.subplots(nrows=2, ncols=2)
axes = axes.ravel()  #get axes
for y in range(len(ids)):
    
    id=[int(a) for a in ids[y]]  # convert to ints

    if id==[]:
        time,ids_un,lat,lon=getobs_drift_byrange(gbox,input_time)  #get  and organize data

    else:
        every_time_total,id_s=[],[]
        totalday=0;total_drifter=0
        region='wv'
        lat_data, lon_data=get_coastline_coordinate(region)  # gets coastline coordinate
        for q in range(len(id)):
        #print id[q]
            time,id_un,lat,lon=getobs_drift_byid(id[q],input_time)  #get  and organize data
            distance=0
            for z in range(len(lat_data)):
                if haversine(lon_data[z], lat_data[z], lon[-1], lat[-1])< 0.5: #1.0 represent  1 kilometer   , get rid of landed drifter
                    #print haversine(lon_data[z], lat_data[z], lon[-1], lat[-1])
                    distance=1
                    break
            if distance==0:
                every_time_total.append(date2num(time[-1])-date2num(time[0]))
                totalday=totalday+date2num(time[-1])-date2num(time[0])  
                total_drifter+=1 # get number of total ploted drifters
        drifter_n,index_day=[],[]    
        for i in range(30): #set y columns to 30 columns
             drifter_n.append(len([x for x in every_time_total if (10*i+10)>x >= (10*i)]))
             index_day.append(str(10*i)+'-'+str(10*i+10))  # for setting y label
         
        df=DataFrame(np.array(drifter_n),index=index_day,columns=[drifter_name[y]])  # generate a dataframe
        ax=axes[y]
        #df.plot(ax=axes[y],title=drifter_name[y],color='r')
        df.plot(ax=axes[y],kind='bar',title=drifter_name[y],ylim=[0,50])  #plot graph
     
        ax.text(0.5, 0.8, 'average '+str(round(totalday/(q+1),1))+' days'+'\nTotal drifters #'+str(total_drifter)+'\nnot include '+str(len(id)-total_drifter)+' drifters ashore',
            verticalalignment='top', horizontalalignment='center',
            transform=ax.transAxes,
            color='green', fontsize=25)
           
        ax.set_xlabel('days_period',fontsize=25)   # set label
        if y==0 or 2:
           ax.set_ylabel('# drifter',fontsize=25)
        #ax.add(rplot.TrellisGrid(['sex', 'smoker']))
        plt.gcf().autofmt_xdate()
        #plt.savefig('EDDIE.png')
#plt.tight_layout()   
plt.show()
