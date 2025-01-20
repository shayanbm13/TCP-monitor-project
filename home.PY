
import typing
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from database import *
from server_tcp import *
from data import *
import sys
import threading
import winsound
import datetime
import re
from persiantools.jdatetime import JalaliDateTime
import pc_ip
import tkinter as tk
from tkinter import messagebox

from final_main import *
class Mainwindow(QtWidgets.QMainWindow):
        conected_ip=str()
        conection_status=False
        coler_left_status=False
        lamp_left_status=False
        generator_left_status=False

        
        temp_1_alarm_status=False
        temp_2_alarm_status=False
        temp_3_alarm_status=False
        temp_4_alarm_status=False
        

        hum_1_alarm_status=False
        hum_2_alarm_status=False
        
        temp_1_is_red=False
        temp_2_is_red=False
        temp_3_is_red=False
        temp_4_is_red=False

        hum_1_is_red=False
        hum_2_is_red=False
        

        #####\

        smoke_alarm_status=False
        motion_alarm_status=False
        door_alarm_status=False

        smoke_is_red=False
        door_is_red=False
        motion_is_red=False
        
        
        previus_phase_1=0
        previus_phase_2=0
        previus_phase_3=0
        
        font_center="5"

        font_adad_bala_paiin="15"
        font_adad_center="12"
        split_stts=0
        light_stts=0
        
        def __init__(self) :
                super().__init__()
                
                QtWidgets.QMainWindow.__init__(self)
                self.ui=Ui_main_window()
                self.ui.setupUi(self)
                self.setMinimumSize(QtCore.QSize(896, 568))
                
                
                def show_error_popup(error):
                        root = tk.Tk()
                        root.withdraw()  # مخفی کردن پنجره اصلی
                       
                        messagebox.showerror("Error", error)

                        # فراخوانی تابع برای نمایش پنجره Popup
                        # show_error_popup()
                ############################ burrons functions  ################
                def coler():
                        if self.conection_status :
                                
                                print(self.coler_left_status)
                                if self.coler_left_status == False :
                                        self.split_stts=1
                                        self.ui.coler_right_5.setStyleSheet("\n""    \n""    \n""    \n""    \n""\n""image: url(:/images/images/phptps/AC-Rait-07-roshan.svg);\n""\n""\n""    border:none;\n""\n""")

                                        self.ui.coler_right_4.setStyleSheet("\n""    \n""    \n""    \n""    \n""\n""image: url(:/images/images/phptps/AC-left-07-roshan.svg);\n""\n""\n""    border:none;\n""\n""")
                                        self.coler_left_status=True
                                elif self.coler_left_status==True :
                                        self.split_stts=0
                                        self.ui.coler_right_5.setStyleSheet("\n""    \n""    \n""    \n""    \n""\n""image: url(:/images/phptps/AC-Rait-07.svg);\n""    background-repeat: none;\n""    background-repeat: none;\n""\n""\n""    border:none;\n""\n""")

                                        self.ui.coler_right_4.setStyleSheet("\n""    \n""    \n""    \n""    \n""\n""image: url(:/images/phptps/AC-left-07.svg);\n""    background-repeat: none;\n""    background-repeat: none;\n""\n""\n""    border:none;\n""\n""")
                                        self.coler_left_status=False
                                msg=split_light(self.split_stts,self.light_stts)                            
                                server = Server()
                                server.send_message_to_clients(msg)
                        else :
                                show_error_popup("لطفا اتصال را چک کنید")   
                def coler_status(status):
                        
                        if status== 1 :
                                
                                self.ui.coler_right_5.setStyleSheet("\n""    \n""    \n""    \n""    \n""\n""image: url(:/images/images/phptps/AC-Rait-07-roshan.svg);\n""\n""\n""    border:none;\n""\n""")

                                self.ui.coler_right_4.setStyleSheet("\n""    \n""    \n""    \n""    \n""\n""image: url(:/images/images/phptps/AC-left-07-roshan.svg);\n""\n""\n""    border:none;\n""\n""")
                                self.coler_left_status=True
                        elif status == 0  :
                                self.ui.coler_right_5.setStyleSheet("\n""    \n""    \n""    \n""    \n""\n""image: url(:/images/phptps/AC-Rait-07.svg);\n""    background-repeat: none;\n""    background-repeat: none;\n""\n""\n""    border:none;\n""\n""")

                                self.ui.coler_right_4.setStyleSheet("\n""    \n""    \n""    \n""    \n""\n""image: url(:/images/phptps/AC-left-07.svg);\n""    background-repeat: none;\n""    background-repeat: none;\n""\n""\n""    border:none;\n""\n""")
                                self.coler_left_status=False
                
                
             
        
        
                def lamp():
                        
                        if self.conection_status :
                
                        
                        
                                if self.lamp_left_status == False :
                                        self.light_stts=1
                                        self.ui.light_down_5.setStyleSheet("\n""    \n""    \n""    \n""        background-repeat: none;\n""image: url(:/images/images/phptps/lamp-02-02-roshan.svg);\n""    \n""    \n""    border:none;\n""")

                                        self.ui.light_down_4.setStyleSheet("\n""    \n""    \n""    \n""    \n""image: url(:/images/images/phptps/lamp-barax-07-roshan-roshan.svg);\n""    background-repeat: none;\n""    \n""    \n""    border:none;\n""")
                                        self.lamp_left_status=True
                                        # add_log("")
                                elif self.lamp_left_status==True :
                                        self.light_stts=0
                                        self.ui.light_down_5.setStyleSheet("\n""    \n""    \n""    \n""        background-repeat: none;\n""image: url(:/images/phptps/lamp-02-02.svg);\n""    \n""    \n""    border:none;\n""")

                                        self.ui.light_down_4.setStyleSheet("\n""    \n""    \n""    \n""    \n""image: url(:/images/phptps/lamp-barax-07.svg);\n""    background-repeat: none;\n""    \n""    \n""    border:none;\n""")
                                        self.lamp_left_status=False 
                                msg=split_light(self.split_stts,self.light_stts)                            
                                server = Server()
                                server.send_message_to_clients(msg)
                        else :
                                show_error_popup("لطفا اتصال را چک کنید")         
                
                def lamp_status(status):
                        
                        
                
                        
                       
                        if status == 1 :
                                self.ui.light_down_5.setStyleSheet("\n""    \n""    \n""    \n""        background-repeat: none;\n""image: url(:/images/images/phptps/lamp-02-02-roshan.svg);\n""    \n""    \n""    border:none;\n""")

                                self.ui.light_down_4.setStyleSheet("\n""    \n""    \n""    \n""    \n""image: url(:/images/images/phptps/lamp-barax-07-roshan-roshan.svg);\n""    background-repeat: none;\n""    \n""    \n""    border:none;\n""")
                                self.lamp_left_status=True
                        elif status == 0 :
                                self.ui.light_down_5.setStyleSheet("\n""    \n""    \n""    \n""        background-repeat: none;\n""image: url(:/images/phptps/lamp-02-02.svg);\n""    \n""    \n""    border:none;\n""")

                                self.ui.light_down_4.setStyleSheet("\n""    \n""    \n""    \n""    \n""image: url(:/images/phptps/lamp-barax-07.svg);\n""    background-repeat: none;\n""    \n""    \n""    border:none;\n""")
                                self.lamp_left_status=False 
                                                

                def generator_status(status):
                        
                        
                
                        
                       
                        if status == 1 :

                                
                                self.ui.light_down_6.setStyleSheet("\n""    \n""    \n""    \n""        background-repeat: none;\n""image: url(:/images/phptps/generator on-01.svg);\n""    \n""    \n""    border:none;\n""")
                                self.ui.motion_detector_5.setStyleSheet("\n""\n""background-color: transparent;\n""image: url(:/images/phptps/alarmha-15.svg);\n""")
                                self.generator_left_status=True
                        elif status == 0 :
                                

                                self.ui.light_down_6.setStyleSheet("\n""    \n""    \n""    \n""        background-repeat: none;\n""image: url(:/images/phptps/generator off-01.svg);\n""    \n""    \n""    border:none;\n""")
                                self.ui.motion_detector_5.setStyleSheet("\n""\n""background-color: transparent;\n""image: url(:/images/phptps/alarmha-20.svg);\n""")
                                self.generator_left_status=False 
                                
                def change_phase_1(status):
                        if status == 1 :
                                        self.previus_phase_1=1
                                        self.ui.label_78.setStyleSheet("\n""\n""        background-color: transparent;\n""    border:none;\n""    image: url(:/images/phptps/display-voltage-03.svg);\n""    ")
                        elif status == 0 :
                                        self.previus_phase_1=0
                                        self.ui.label_78.setStyleSheet("\n""\n""        background-color: transparent;\n""    border:none;\n""    image: url(:/images/phptps/display-voltage-02.svg);\n""    ")
                def change_phase_2(status):
                        if status == 1 :
                                        self.previus_phase_2=1
                                        self.ui.label_82.setStyleSheet("\n""\n""        background-color: transparent;\n""    border:none;\n""    image: url(:/images/phptps/display-voltage-03.svg);\n""    ")
                        elif status == 0 :
                                        self.previus_phase_2=0
                                        self.ui.label_82.setStyleSheet("\n""\n""        background-color: transparent;\n""    border:none;\n""    image: url(:/images/phptps/display-voltage-02.svg);\n""    ")
                def change_phase_3(status):
                        if status == 1 :
                                        self.previus_phase_3=1
                                        self.ui.label_86.setStyleSheet("\n""\n""        background-color: transparent;\n""    border:none;\n""    image: url(:/images/phptps/display-voltage-03.svg);\n""    ")
                        elif status == 0 :
                                        self.previus_phase_3=0
                                        self.ui.label_86.setStyleSheet("\n""\n""        background-color: transparent;\n""    border:none;\n""    image: url(:/images/phptps/display-voltage-02.svg);\n""    ")                            
                
                
                currentt_db=current_db()
                cr_data=currentt_db.read_data()
                print(cr_data)
                self.ui.temp_down_46.setText(cr_data[0][1])
                self.ui.temp_down_49.setText(cr_data[0][2])
                self.ui.temp_down_53.setText(cr_data[0][3])
                self.ui.temp_down_52.setText(cr_data[0][4])
                
                self.ui.temp_down_47.setText(cr_data[0][5])
                self.ui.temp_down_51.setText(cr_data[0][6])
                
                coler_status(cr_data[0][7])
                lamp_status(cr_data[0][8])
                generator_status(cr_data[0][9])
                
                self.smoke_alarm_status=cr_data[0][10]
                self.motion_alarm_status=cr_data[0][11]
                self.door_alarm_status=cr_data[0][12]
                
       
                self.ui.voltage_9.setText(f"Voltage: {str(cr_data[0][13])}")
                self.ui.voltage_10.setText(f"Voltage: {str(cr_data[0][14])}")
                self.ui.voltage_11.setText(f"Voltage: {str(cr_data[0][15])}")

                self.ui.amper_5.setText(f"Current: {str(cr_data[0][16])}")
                self.ui.amper_6.setText(f"Current: {str(cr_data[0][17])}")
                self.ui.voltage_12.setText(f"Current: {str(cr_data[0][18])}")
                self.ui.voltage_13.setText(f"Air conditioner current : {str(cr_data[0][19])}")
                
                change_phase_1(cr_data[0][20])
                change_phase_2(cr_data[0][21])
                change_phase_3(cr_data[0][22])
                
                
                smart_home_db1 = SmartHomeDatabase()
                smart_home_db1.create_database()
                data1 = smart_home_db1.read_data()
                
                exists1 = smart_home_db.check_data_existence(1)
                if exists1 : 
                        self.ui.temp_down_40.setText(str(data1[0][1]))
                        self.ui.temp_down_33.setText(str(data1[0][3]))
                        self.ui.temp_down_35.setText(str(data1[0][5]))
                        self.ui.temp_down_45.setText(str(data1[0][6]))

                
                        self.ui.temp_down_41.setText(str(data1[0][2]))
                        self.ui.temp_down_34.setText(str(data1[0][4]))
                else : 
                        self.ui.temp_down_40.setText("--")
                        self.ui.temp_down_33.setText("--")
                        self.ui.temp_down_35.setText("--")
                        self.ui.temp_down_45.setText("--")

            
                        self.ui.temp_down_41.setText("--")
                        self.ui.temp_down_34.setText("--")
                
                
                def go_setting():
                        
                        self.ui.stackedWidget.setCurrentWidget(self.ui.setting_page)
                        get_data()
                        
                ######################## buttons ########################
                
                self.ui.pushButton.clicked.connect(lambda: go_setting())
                self.ui.pushButton_2.clicked.connect(lambda: go_setting())
                self.ui.pushButton_3.clicked.connect(lambda: go_setting())
                
                
                self.ui.coler_right_4.clicked.connect(lambda: coler())
                self.ui.coler_right_5.clicked.connect(lambda: coler())
                self.ui.light_down_5.clicked.connect(lambda: lamp())
                self.ui.light_down_4.clicked.connect(lambda: lamp())
                
                self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        
                self.ui.pushButton_5.clicked.connect(lambda : set_data())
                # self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
                
                
                
                ######################## UI ########################
                self.ui.label_73.setText(get_local_IP())
                
                def log_date_and_time():
                        

                        # گرفتن تاریخ و زمان فعلی
                        current_datetime = JalaliDateTime.now()

                        # تبدیل تاریخ و زمان فعلی به فرمت موردنظر
                        formatted_datetime = current_datetime.strftime('%Y/%m/%d // %H:%M:%S')
                        return formatted_datetime

                
                def time():
                        current_time = datetime.datetime.now()
                        hour = current_time.strftime("%H")
                        minute = current_time.strftime("%M")
                        if int(hour) > 12 :
                                 self.ui.label_70.setText("PM")
                        else :
                                 self.ui.label_70.setText("AM")
                                 
                        self.ui.label_69.setText(f"{hour}:{minute}") 
                        
                def time_for_client():
                        current_time = datetime.datetime.now()
                        hour = current_time.strftime("%H")
                        minute = current_time.strftime("%M")
   
                        return hour , minute
                
                def add_log(log_txt):
                        smart_home_db = SmartHomeDatabase()
                        smart_home_db.create_database()
                        data = smart_home_db.read_data()
                        log_path= data[0][11]+"/Griffin_log.txt"
                        # print(data[0][0])
                        
                        try:
                                
                        
                                with open(log_path, 'a+', encoding='utf-8')as file:
                                        file.seek(0)  # رفتن به ابتدای فایل
                                        lines = file.readlines()
                                        line_count = len(lines)

                                        if line_count >= 1500:
                                                file.truncate(0) 
                                        file.write(log_txt + "\n")
                                        
                        except: 
                                None
         
                def decode_0_1(code):
                        if code==0 :
                                return "خاموش"
                        elif code==1:
                                return "روشن"
                def decode_true_false(code):
                        if code==True :
                                return 1
                        elif code==False:
                                return 0
                
                def select_folder():
                        options = QtWidgets.QFileDialog.Options()
                        options |= QtWidgets.QFileDialog.DontUseNativeDialog
                        folder_dialog = QtWidgets.QFileDialog()
                        folder_dialog.setOptions(options)
                        selected_folder = folder_dialog.getExistingDirectory(self, "select log location", "/")  # مسیر ابتدایی
                        if selected_folder:
                                print("selected folder :", selected_folder)
                                self.ui.curent_temp_label_41.setText(selected_folder)
                                
                                # اینجا می‌توانید با استفاده از مسیر فولدر انتخاب شده، عملیات خود را انجام دهید
                self.ui.pushButton_4.clicked.connect(lambda : select_folder())
                
            
                def message_receive_cheker():
                        server2= Server()
                        received_message=server2.received_message
                        if received_message.__len__() > 0 :
                                
                                # data=eval(received_message[0])[0]
                                
                                data=msg_convertor(received_message[0])

                                
                        ################## Alarms ##################
                           ####### temp  #######
                                set_temp_1=data["set_temp1"]
                                set_temp_2=data["set_temp2"]
                                set_temp_3=data["set_temp3"]
                                set_temp_4=data["set_temp4"]
                                current_temp_1=data["current_temp1"]
                                current_temp_2=data["current_temp2"]
                                current_temp_3=data["current_temp3"]
                                current_temp_4=data["current_temp4"]
                           ####### hum  #######
                                set_hum_1=data["set_hum1"]
                                set_hum_2=data["set_hum2"]
                                current_hum_1=data["current_hum1"]
                                current_hum_2=data["current_hum2"]
                        
                           ####### sensors  #######       
                                smoke=data["smoke"]
                                door=data["door"]
                                motion=data["motion"]        
                                
                               
  
   
                                previus_voltage_9= re.findall(r'\d+', self.ui.voltage_9.text())
                                previus_voltage_10 = re.findall(r'\d+', self.ui.voltage_10.text())
                                previus_voltage_11=  re.findall(r'\d+', self.ui.voltage_11.text())
                               
                                previus_amper_5 = re.findall(r'\d+', self.ui.amper_5.text())
                                previus_amper_6 = re.findall(r'\d+', self.ui.amper_6.text())
                                previus_voltage_12=  re.findall(r'\d+', self.ui.voltage_12.text())
                                
       
                                

                                
                                previus_temp_down_40=re.findall(r'\d+', self.ui.temp_down_40.text())
                                previus_temp_down_33=re.findall(r'\d+', self.ui.temp_down_33.text())
                                previus_temp_down_35=re.findall(r'\d+', self.ui.temp_down_35.text())
                                previus_temp_down_45=re.findall(r'\d+', self.ui.temp_down_45.text())
                                
                                previus_temp_down_41=re.findall(r'\d+', self.ui.temp_down_41.text())
                                previus_temp_down_34=re.findall(r'\d+', self.ui.temp_down_34.text())
                                
                                
                                previus_temp_down_46=re.findall(r'\d+', self.ui.temp_down_46.text())
                                previus_temp_down_49=re.findall(r'\d+', self.ui.temp_down_49.text())
                                previus_temp_down_53=re.findall(r'\d+', self.ui.temp_down_53.text())
                                previus_temp_down_52=re.findall(r'\d+', self.ui.temp_down_52.text())
                                
                                
                                previus_temp_down_47=re.findall(r'\d+', self.ui.temp_down_47.text())
                                previus_temp_down_51=re.findall(r'\d+', self.ui.temp_down_51.text())
                                
                                previus_voltage_13=  re.findall(r'\d+', self.ui.voltage_13.text())
                                
                                
                                
                                
                                
                                
                                
                        ################## voltage ##################
                                self.ui.voltage_9.setText(f"Voltage: {str(data["voltage1"])}")
                                self.ui.voltage_10.setText(f"Voltage: {str(data["voltage2"])}")
                                self.ui.voltage_11.setText(f"Voltage: {str(data["voltage3"])}")
                        ################## current ##################         
                                self.ui.amper_5.setText(f"Current: {str(data["current1"])}")
                                self.ui.amper_6.setText(f"Current: {str(data["current2"])}")
                                self.ui.voltage_12.setText(f"Current: {str(data["current3"])}")
                                
                        ################## phase ##################
                                
                                change_phase_1(data["phase1"])
                                change_phase_2(data["phase2"])
                                change_phase_3(data["phase3"])
                                
                        ################## set temp ##################
                                self.ui.temp_down_40.setText(str(data["set_temp1"]))
                                self.ui.temp_down_33.setText(str(data["set_temp2"]))
                                self.ui.temp_down_35.setText(str(data["set_temp3"]))
                                self.ui.temp_down_45.setText(str(data["set_temp4"]))

                        ################## set hum ##################
                                self.ui.temp_down_41.setText(str(data["set_hum1"]))
                                self.ui.temp_down_34.setText(str(data["set_hum2"]))
                                
                        ################## current temp ##################
                                self.ui.temp_down_46.setText(str(data["current_temp1"]))
                                self.ui.temp_down_49.setText(str(data["current_temp2"]))
                                self.ui.temp_down_53.setText(str(data["current_temp3"]))
                                self.ui.temp_down_52.setText(str(data["current_temp4"]))
                                
                        ################## current hum ##################
                                self.ui.temp_down_47.setText(str(data["current_hum1"]))
                                self.ui.temp_down_51.setText(str(data["current_hum2"]))     
                        ################## current spiler ##################
                                self.ui.voltage_13.setText(f"Air conditioner current : {str(data["split_current"])}")
                                                     
                        ################## lamp & spilet & generator ##################       
                                coler_status(data["split"])
                                lamp_status(data["light"])
                                generator_status(data["generator"])
                                
                        ################## Database ##################        
                                smart_home_db = SmartHomeDatabase()
                                smart_home_db.create_database()
                                
                                exists = smart_home_db.check_data_existence(1)
                                current_dbs=current_db()
                                current_dbs.create_database()
                                current_dbs.update_data(1,data["current_temp1"],data["current_temp2"],data["current_temp3"],data["current_temp4"],data["current_hum1"],data["current_hum2"],data["split"],data["light"],data["generator"],data["smoke"],data["motion"],data["door"],data["voltage1"],data["voltage2"],data["voltage3"],data["current1"],data["current2"],data["current3"],data["split_current"],data["phase1"],data["phase2"],data["phase3"])
                                if exists:
                                        database_data = smart_home_db.read_data()
                                        smart_home_db.update_data(1, data["set_temp1"], data["set_hum1"], data["set_temp2"], data["set_hum2"], data["set_temp3"], data["set_temp4"], database_data[0][7], database_data[0][8], database_data[0][9], database_data[0][10], database_data[0][11])

                                else:
                                        smart_home_db.insert_data(  data["set_temp1"], data["set_hum1"], data["set_temp2"], data["set_hum2"], data["set_temp3"], data["set_temp4"], get_local_IP(), 00, 00, 00, "//")

                                print(received_message[0]) 
                                server2.received_message.clear()
                                
                                
                                
                                if len(previus_voltage_9) > 0 :
                                        if data["voltage1"] != int(previus_voltage_9[0]) :
                                                add_log(f"({log_date_and_time()}) ======== تغییر ولتاژ1 از {int(previus_voltage_9[0])} به {data["voltage1"]} ")
                                if len(previus_voltage_10) > 0 :                
                                        if data["voltage2"] != int(previus_voltage_10[0]) :
                                                add_log(f"({log_date_and_time()}) ======== تغییر ولتاژ2 از {int(previus_voltage_10[0])} به {data["voltage2"]} ")         
                                if len(previus_voltage_11) > 0 :
                                        if data["voltage3"] != int(previus_voltage_11[0]) :
                                                add_log(f"({log_date_and_time()}) ======== تغییر ولتاژ3 از {int(previus_voltage_11[0])} به {data["voltage3"]} ")         
                                if len(previus_amper_5) > 0 :              
                                        if data["current1"] != int(previus_amper_5[0]) :
                                                add_log(f"({log_date_and_time()}) ======== تغییر آمپر1 از {int(previus_amper_5[0])} به {data["current1"]} ")         
                                if len(previus_amper_6) > 0 :                              
                                        if data["current2"] != int(previus_amper_6[0]) :
                                                add_log(f"({log_date_and_time()}) ======== تغییر آمپر2 از {int(previus_amper_6[0])} به {data["current2"]} ")         
                                if len(previus_voltage_12) > 0 :                                         
                                        if data["current3"] != int(previus_voltage_12[0]) :
                                                add_log(f"({log_date_and_time()}) ======== تغییر آمپر3 از {int(previus_voltage_12[0])} به {data["current3"]} ")         
                                if  self.previus_phase_1 != 5 :    
                                        if data["phase1"] != int(self.previus_phase_1) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر فاز1 از {decode_0_1(int(self.previus_phase_1[0]))} به {decode_0_1(data["phase1"])} ")         
                                if  self.previus_phase_2 != 5 :      
                                        if data["phase2"] != int(self.previus_phase_2) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر فاز2 از {decode_0_1(int(self.previus_phase_2[0]))} به {decode_0_1(data["phase2"])} ")         
                                if  self.previus_phase_3 != 5 :   
                                        if data["phase3"] != int(self.previus_phase_3) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر فاز3 از {decode_0_1(int(self.previus_phase_3[0]))} به {decode_0_1(data["phase3"])} ")         
                                if len(previus_voltage_13) > 0 :   
                                        if data["split_current"] != int(previus_voltage_13[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر جریان اسپیلت از {int(previus_voltage_13[0])} به {data["split_current"]} ")         


                                if len(previus_temp_down_40) > 0 :   
                                        if data["set_temp1"] != int(previus_temp_down_40[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر دمای ست شده1 از {int(previus_temp_down_40[0])} به {data["set_temp1"]} ")         
                                if len(previus_temp_down_33) > 0 :  
                                        if data["set_temp2"] != int(previus_temp_down_33[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر دمای ست شده2 از {int(previus_temp_down_33[0])} به {data["set_temp2"]} ")         
                                if len(previus_temp_down_35) > 0 :  
                                        if data["set_temp3"] != int(previus_temp_down_35[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر دمای ست شده3 از {int(previus_temp_down_35[0])} به {data["set_temp3"]} ")         
                                if len(previus_temp_down_45) > 0 : 
                                        if data["set_temp4"] != int(previus_temp_down_45[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر دمای ست شده4 از {int(previus_temp_down_45[0])} به {data["set_temp4"]} ")         

                                if len(previus_temp_down_41) > 0 : 
                                        if data["set_hum1"] != int(previus_temp_down_41[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر رطوبت ست شده1 از {int(previus_temp_down_41[0])} به {data["set_hum1"]} ")         
                                if len(previus_temp_down_34) > 0 : 
                                        if data["set_hum2"] != int(previus_temp_down_34[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر رطوبت ست شده2 از {int(previus_temp_down_34[0])} به {data["set_hum2"]} ")         
                                if len(previus_temp_down_46) > 0 : 
                                        if data["current_temp1"] != int(previus_temp_down_46[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر دمای فعلی1 از {int(previus_temp_down_46[0])} به {data["current_temp1"]} ")         
                                if len(previus_temp_down_49) > 0 : 
                                        if data["current_temp2"] != int(previus_temp_down_49[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر دمای فعلی2 از {int(previus_temp_down_49[0])} به {data["current_temp2"]} ")         
                                if len(previus_temp_down_53) > 0 : 
                                        if data["current_temp3"] != int(previus_temp_down_53[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر دمای فعلی3 از {int(previus_temp_down_53[0])} به {data["current_temp3"]} ")         
                                if len(previus_temp_down_52) > 0 : 
                                        if data["current_temp4"] != int(previus_temp_down_52[0]) :
                                                        
                                                add_log(f"({log_date_and_time()}) ======== تغییر دمای فعلی4 از {int(previus_temp_down_52[0])} به {data["current_temp4"]} ")         
                                if len(previus_temp_down_47) > 0 : 
                                        if data["current_hum1"] != int(previus_temp_down_47[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر رطوبت فعلی1 از {int(previus_temp_down_47[0])} به {data["current_hum1"]} ")         
                                if len(previus_temp_down_51) > 0 : 
                                        if data["current_hum2"] != int(previus_temp_down_51[0]) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر رطوبت فعلی2 از {int(previus_temp_down_51[0])} به {data["current_hum2"]} ")         
                                if  self.lamp_left_status != 5 : 
                                        if data["light"] != int(decode_true_false(self.lamp_left_status)) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر وضعیت لامپ از {decode_0_1(decode_true_false(self.lamp_left_status))} به {decode_0_1(data["light"])} ")         
                                if  self.coler_left_status != 5 : 
                                        if data["split"] != int(decode_true_false(self.coler_left_status)) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر وضعیت اسپلیت از {decode_0_1(decode_true_false(self.coler_left_status))} به {decode_0_1(data["split"])} ")         
                                if  self.generator_left_status != 5 : 
                                        if data["generator"] != int(decode_true_false(self.generator_left_status)) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر وضعیت ژنراتور از {decode_0_1(decode_true_false(self.generator_left_status))} به {decode_0_1(data["generator"])} ")         
                                if  self.smoke_alarm_status != 5 : 
                                        if smoke != int(decode_true_false(self.smoke_alarm_status)) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر وضعیت آلارم دود از {decode_0_1(decode_true_false(self.smoke_alarm_status))} به {decode_0_1(smoke)} ")         
                                if  self.door_alarm_status != 5 : 
                                        if door != int(decode_true_false(self.door_alarm_status)) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر وضعیت آلارم درب از {decode_0_1(decode_true_false(self.door_alarm_status))} به {decode_0_1(door)} ")         
                                if  self.motion_alarm_status != 5 : 
                                        if motion != int(decode_true_false(self.motion_alarm_status)) :
                                                
                                                add_log(f"({log_date_and_time()}) ======== تغییر وضعیت آلارم حرکتی از {decode_0_1(decode_true_false(self.motion_alarm_status))} به {decode_0_1(motion)} ")         



                                if current_temp_1 > set_temp_1 :
                                        self.temp_1_alarm_status=True
                                elif current_temp_1 < set_temp_1 :
                                        self.temp_1_alarm_status=False
                                        


                                if current_temp_2 > set_temp_2 :
                                        self.temp_2_alarm_status=True
                                elif current_temp_2 < set_temp_2 :
                                        self.temp_2_alarm_status=False                                        
                                
                                
                                
                                if current_temp_3 > set_temp_3 :
                                        self.temp_3_alarm_status=True               
                                elif current_temp_3 < set_temp_3 :
                                        self.temp_3_alarm_status=False                                    
                                
                                if current_temp_4 > set_temp_4 :
                                        self.temp_4_alarm_status=True                                      
                                elif current_temp_4 < set_temp_4 :
                                        self.temp_4_alarm_status=False                        
                                
                                
                                
                                
                                if current_hum_1 > set_hum_1 :
                                        self.hum_1_alarm_status=True
                                elif current_hum_1 < set_hum_1 :
                                        self.hum_1_alarm_status=False
                                        


                                if current_hum_2 > set_hum_2 :
                                        self.hum_2_alarm_status=True
                                elif current_hum_2 < set_hum_2 :
                                        self.hum_2_alarm_status=False       
                                        
                                if smoke == 1 :
                                        self.smoke_alarm_status=True
                                elif smoke == 0:
                                        self.smoke_alarm_status=False                     

                                if door == 1 :
                                        self.door_alarm_status=True
                                elif door == 0:
                                        self.door_alarm_status=False    



                                if motion == 1 :
                                        self.motion_alarm_status=True
                                elif motion == 0:
                                        self.motion_alarm_status=False   

                        
                        else :
                                None
                        

                
                #########  timers  #########
                
                
                self.server = Server()
                self.client_check_timer = QtCore.QTimer(self)
                self.client_check_timer.timeout.connect(self.check_clients)
                self.client_check_timer.start(1000)  # هر ثانیه وضعیت کلاینت‌ها بررسی شود
                
                
                self.update_cheker= QtCore.QTimer(self)
                self.update_cheker.timeout.connect(message_receive_cheker)
                self.update_cheker.start(1000)
                
                self.alarm_cheker_timer= QtCore.QTimer(self)
                self.alarm_cheker_timer.timeout.connect(self.all_alarm_cheker)
                self.alarm_cheker_timer.start(1000)
                
                self.clock= QtCore.QTimer(self)
                self.clock.timeout.connect(time)
                self.clock.start(1000)
 
                        

######################## inputs ########################
                def get_data():
                        
                        
                        smart_home_db = SmartHomeDatabase()
                        smart_home_db.create_database()
                        data = smart_home_db.read_data()
                        # print(data[0][0])
                        
                        try:
                                self.ui.lineEdit_7.setText(str(data[0][1])) 
                                self.ui.lineEdit_5.setText(str(data[0][2])) 
                                self.ui.lineEdit_6.setText(str(data[0][3])) 
                                self.ui.lineEdit_8.setText(str(data[0][4])) 
                                self.ui.lineEdit_9.setText(str(data[0][5])) 
                                self.ui.lineEdit_10.setText(str(data[0][6])) 
                                self.ui.lineEdit.setText(str(data[0][7])) 
                                self.ui.lineEdit_2.setText(str(data[0][8])) 
                                self.ui.lineEdit_3.setText(str(data[0][9])) 
                                self.ui.lineEdit_4.setText(str(data[0][10])) 
                                self.ui.curent_temp_label_41.setText(str(data[0][11])) 
                        except:
                                print("database is empty")
                                self.ui.lineEdit.setText(get_local_IP()) 
                        
                        
                        
                
                # print(set_humidity_1)
                

                
                def set_data():
                        
                        set_temp_1 = self.ui.lineEdit_7.text()
                        set_humidity_1 = self.ui.lineEdit_5.text()
                        set_temp_2 = self.ui.lineEdit_6.text()
                        set_humidity_2 = self.ui.lineEdit_8.text()
                        set_temp_3 = self.ui.lineEdit_9.text()
                        set_temp_4 = self.ui.lineEdit_10.text()
                        set_ip = self.ui.lineEdit.text()
                        phone_num_1 = self.ui.lineEdit_2.text()
                        phone_num_2 = self.ui.lineEdit_3.text()
                        phone_num_3 = self.ui.lineEdit_4.text()
                        database_path = self.ui.curent_temp_label_41.text()
                        if self.conection_status :

                                if (set_temp_1 != "") & (set_humidity_1 != "") & (set_temp_2 != "") & (set_humidity_2 != "") & (set_temp_3 != "")  & (set_temp_4 != "") & (set_ip != "") & (phone_num_1 != "") & (phone_num_2 != "") & (phone_num_3 != "") & (database_path!="") :
                                        
                                        smart_home_db = SmartHomeDatabase()

                                        smart_home_db.create_database()
                                        hour , minute = time_for_client()
                                        
                                        exists = smart_home_db.check_data_existence(1)

                                        if exists:
                                                path=""
                                                if database_path =="":
                                                        path="//"
                                                else:
                                                        path=database_path
                                                        
                                                smart_home_db.update_data(1, set_temp_1, set_humidity_1, set_temp_2, set_humidity_2, set_temp_3, set_temp_4, set_ip, phone_num_1, phone_num_2, phone_num_3, path)
                                                print("database updated")
                                                
                                                data=data_coder(set_temp_1, set_humidity_1, set_temp_2, set_humidity_2, set_temp_3, set_temp_4, phone_num_1, phone_num_2, phone_num_3,hour, minute)
                                                server = Server()
                                                server.send_message_to_clients(data)
                                        else:
                                                path=""
                                                if database_path =="":
                                                        path="//"
                                                else:
                                                        path=database_path
                                        
                                                smart_home_db.insert_data( set_temp_1, set_humidity_1, set_temp_2, set_humidity_2, set_temp_3, set_temp_4, set_ip, phone_num_1, phone_num_2, phone_num_3, path)
                                                print("database created")
                                                data=data_coder(set_temp_1, set_humidity_1, set_temp_2, set_humidity_2, set_temp_3, set_temp_4, phone_num_1, phone_num_2, phone_num_3,hour, minute)
                                                server = Server()
                                                server.send_message_to_clients(data)
                                        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
                                else:
                                        show_error_popup("لطفا همه ی موارد را پر کنید")
                        else :
                                show_error_popup("لطفا اتصال را چک کنید")          
                self.show()      

        def beep_alarm(self):
                frequency = 1500  
                duration = 300
                winsound.Beep(frequency, duration)    
                # time.sleep(500)
                        

        def all_alarm_cheker(self):
                if self.temp_1_alarm_status :
                        if self.temp_1_is_red :
                                
                                self.ui.temp_down_46.setStyleSheet("#temp_down_46{\n""	color: white;\n"f"font:{self.font_adad_bala_paiin}pt;\n""\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_51.setStyleSheet("\n""    \n""	color: white;\n""    \n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                                self.temp_1_is_red=False
                                self.beep_alarm()
                        elif not self.temp_1_is_red :
                                
                                self.ui.temp_down_46.setStyleSheet("#temp_down_46{\n""color: rgb(255, 0, 0);\n"f"font:{self.font_adad_bala_paiin}pt;\n""\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_51.setStyleSheet("\n""    \n""color: rgb(255, 0, 0);\n""    \n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-13.svg);\n""")
                                self.temp_1_is_red=True
                                self.beep_alarm()
                elif not self.temp_1_alarm_status :  
                        
                        if self.temp_1_is_red :
                                self.temp_1_is_red=False
                                self.ui.temp_down_46.setStyleSheet("#temp_down_46{\n""	color: white;\n"f"font:{self.font_adad_bala_paiin}pt;\n""\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_51.setStyleSheet("\n""    \n""	color: white;\n""    \n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                        else:
                                None           
                
                
                if self.temp_2_alarm_status :
                        if self.temp_2_is_red :
                                
                                self.ui.temp_down_49.setStyleSheet("#temp_down_49{\n""	color: white;\n"f"font:{self.font_adad_bala_paiin}pt;\n""\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_53.setStyleSheet("\n""    \n""	color: white;\n""    \n""")   
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                                self.temp_2_is_red=False
                                self.beep_alarm()
                        elif not self.temp_2_is_red :
                                
                                self.ui.temp_down_49.setStyleSheet("#temp_down_49{\n""color: rgb(255, 0, 0);\n"f"font:{self.font_adad_bala_paiin}pt;\n""\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_53.setStyleSheet("\n""    \n""color: rgb(255, 0, 0);\n""    \n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-13.svg);\n""")
                                self.temp_2_is_red=True
                                self.beep_alarm()
                                
                elif not self.temp_2_alarm_status :  
                        
                        if self.temp_2_is_red :
                                self.temp_2_is_red=False
                                self.ui.temp_down_49.setStyleSheet("#temp_down_49{\n""	color: white;\n"f"font:{self.font_adad_bala_paiin}pt;\n""\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_53.setStyleSheet("\n""    \n""	color: white;\n""    \n""")  
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                        else:
                                None                
                
                
                if self.temp_3_alarm_status :
                        if self.temp_3_is_red :
                                
                                self.ui.temp_down_53.setStyleSheet("#temp_down_53{\n""     color: white;\n"f"font:{self.font_adad_center}pt;\n""\n""}\n""\n""\n""")
                                self.ui.label_103.setStyleSheet("\n""\n""#label_103{\n""background-color:none;\n""color: white;\n"f"font:{self.font_center}pt;\n""\n""\n""}\n""\n""\n""") 
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                                self.temp_3_is_red=False
                                self.beep_alarm()
                        elif not self.temp_3_is_red :
                                
                                self.ui.temp_down_53.setStyleSheet("#temp_down_53{\n""     color: rgb(255, 0, 0);\n"f"font:{self.font_adad_center}pt;\n""\n""}\n""\n""\n""")
                                self.ui.label_103.setStyleSheet("\n""\n""#label_103{\n""background-color:none;\n""color: rgb(255, 0, 0);"f"font:{self.font_center}pt;\n""\n""\n""}\n""\n""\n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-13.svg);\n""")
                                self.temp_3_is_red=True
                                self.beep_alarm()
                                
                elif not self.temp_3_alarm_status :  
                        
                        if self.temp_3_is_red :
                                self.temp_3_is_red=False
                                self.ui.temp_down_53.setStyleSheet("#temp_down_53{\n""     color: white;\n"f"font:{self.font_adad_center}pt;\n""\n""}\n""\n""\n""")
                                self.ui.label_103.setStyleSheet("\n""\n""#label_103{\n""background-color:none;\n""color: white;\n"f"font:{self.font_center}pt;\n""\n""\n""}\n""\n""\n""") 
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                        else:
                                None                                     
                     
                     
                if self.temp_4_alarm_status :
                        if self.temp_4_is_red :
                                
                                self.ui.temp_down_52.setStyleSheet("#temp_down_52{\n""     color: white;\n"f"font:{self.font_adad_center}pt;\n""\n""}\n""\n""\n""")
                                self.ui.label_99.setStyleSheet("\n""\n""#label_99{\n""background-color:none;\n""color: white;\n"f"font:{self.font_center}pt;\n""\n""\n""}\n""\n""\n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                                self.temp_4_is_red=False
                                self.beep_alarm()
                        elif not self.temp_4_is_red :
                                
                                self.ui.temp_down_52.setStyleSheet("#temp_down_52{\n""     color: rgb(255, 0, 0);\n"f"font:{self.font_adad_center}pt;\n""\n""}\n""\n""\n""")
                                self.ui.label_99.setStyleSheet("\n""\n""#label_99{\n""background-color:none;\n""color: rgb(255, 0, 0);\n"f"font:{self.font_center}pt;\n""\n""\n""}\n""\n""\n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-13.svg);\n""")
                                self.temp_4_is_red=True
                                self.beep_alarm()
                                
                elif not self.temp_4_alarm_status :  
                        
                        if self.temp_4_is_red :
                                self.temp_4_is_red=False
                                self.ui.temp_down_52.setStyleSheet("#temp_down_52{\n""     color: white;\n"f"font:{self.font_adad_center}pt;\n""\n""}\n""\n""\n""")
                                self.ui.label_99.setStyleSheet("\n""\n""#label_99{\n""background-color:none;\n""color: white;\n"f"font:{self.font_center}pt;\n""\n""\n""}\n""\n""\n""") 
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                        else:
                                None           
                        

                    

                if self.hum_1_alarm_status :
                        if self.hum_1_is_red :
                                
                                self.ui.temp_down_47.setStyleSheet("#temp_down_47{\n""     color: white;\n"f"font:{self.font_adad_bala_paiin}pt;\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_52.setStyleSheet("\n""    \n""    color: white;\n""    \n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                                self.hum_1_is_red=False
                                self.beep_alarm()
                        elif not self.hum_1_is_red :
                                
                                self.ui.temp_down_47.setStyleSheet("#temp_down_47{\n""     color: rgb(255, 0, 0);\n"f"font:{self.font_adad_bala_paiin}pt;\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_52.setStyleSheet("\n""    \n""    color: rgb(255, 0, 0);\n""    \n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-13.svg);\n""")
                                self.hum_1_is_red=True
                                self.beep_alarm()
                                
                elif not self.hum_1_alarm_status :  
                        
                        if self.hum_1_is_red :
                                self.ui.temp_down_47.setStyleSheet("#temp_down_47{\n""     color: white;\n"f"font:{self.font_adad_bala_paiin}pt;\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_52.setStyleSheet("\n""    \n""    color: white;\n""    \n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                        else:
                                None           
                        
                        
                    
                if self.hum_2_alarm_status :
                        if self.hum_2_is_red :
                                
                                self.ui.temp_down_51.setStyleSheet("#temp_down_51{\n""     color: white;\n"f"font:{self.font_adad_bala_paiin}pt;\n""\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_54.setStyleSheet("\n""    \n""    color: white;\n""    \n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                                self.hum_2_is_red=False
                                self.beep_alarm()
                        elif not self.hum_2_is_red :
                                
                                self.ui.temp_down_51.setStyleSheet("#temp_down_51{\n""     color: rgb(255, 0, 0);\n"f"font:{self.font_adad_bala_paiin}pt;\n""\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_54.setStyleSheet("\n""    \n""    color: rgb(255, 0, 0);\n""    \n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-13.svg);\n""")
                                self.hum_2_is_red=True
                                self.beep_alarm()
                                
                elif not self.hum_2_alarm_status :  
                        
                        if self.hum_2_is_red :
                                self.ui.temp_down_51.setStyleSheet("#temp_down_51{\n""     color: white;\n"f"font:{self.font_adad_bala_paiin}pt;\n""\n""}\n""\n""\n""")
                                self.ui.curent_temp_label_54.setStyleSheet("\n""    \n""    color: white;\n""    \n""")
                                self.ui.temp_warning_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    image: url(:/images/phptps/alarmha-18.svg);\n""")
                        else:
                                None           
                           
                        

                        


                if self.smoke_alarm_status== True  :
                        if self.smoke_is_red :
                                
                                self.ui.smok_down_3.setStyleSheet("\n""    \n""    image: url(:/images/phptps/smoke off-01.svg);\n""    background-repeat: none;\n""\n""        \n""margin-top:35;\n""    border:none;\n""")
                                self.ui.smoke_detector_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    \n""    \n""    \n""    image: url(:/images/phptps/alarmha-17.svg);\n""\n""")
                                self.smoke_is_red=False
                                self.beep_alarm()
                        elif not self.smoke_is_red :
                                
                                self.ui.smok_down_3.setStyleSheet("\n""    \n""    image: url(:/images/phptps/smoke on-01.svg);\n""    background-repeat: none;\n""\n""        \n""margin-top:35;\n""    border:none;\n""")
                                self.ui.smoke_detector_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    \n""    \n""    \n""    image: url(:/images/phptps/alarmha-12.svg);\n""\n""")
                                self.smoke_is_red=True
                                self.beep_alarm()
                                
                elif not self.smoke_alarm_status :  
                        
                        if self.smoke_is_red :
                                self.smoke_is_red=False
                                self.ui.smok_down_3.setStyleSheet("\n""    \n""    image: url(:/images/phptps/smoke off-01.svg);\n""    background-repeat: none;\n""\n""        \n""margin-top:35;\n""    border:none;\n""")
                                self.ui.smoke_detector_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    \n""    \n""    \n""    image: url(:/images/phptps/alarmha-17.svg);\n""\n""")
                        else:
                                None         



                if self.motion_alarm_status== True  :
                        if self.motion_is_red :
                                
                                self.ui.smok_up_3.setStyleSheet("\n""    \n""    \n""    image: url(:/images/phptps/motion off-01.svg);\n""    background-repeat: none;\n""\n""        \n""margin-bottom:35;\n""    border:none;\n""")
                                self.ui.motion_detector_6.setStyleSheet("\n""\n""\n""background-color: transparent;\n""    image: url(:/images/phptps/alarmha-19.svg);\n""")
                                self.motion_is_red=False
                                self.beep_alarm()
                        elif not self.motion_is_red :
                                
                                self.ui.smok_up_3.setStyleSheet("\n""    \n""    \n""    image: url(:/images/phptps/motion on-01.svg);\n""    background-repeat: none;\n""\n""        \n""margin-bottom:35;\n""    border:none;\n""")
                                self.ui.motion_detector_6.setStyleSheet("\n""\n""\n""background-color: transparent;\n""    image: url(:/images/phptps/alarmha-14.svg);\n""")
                                self.motion_is_red=True
                                self.beep_alarm()
                                
                elif not self.motion_alarm_status :  
                        
                        if self.motion_is_red :
                                self.motion_is_red=False
                                self.ui.smok_up_3.setStyleSheet("\n""    \n""    \n""    image: url(:/images/phptps/motion off-01.svg);\n""    background-repeat: none;\n""\n""        \n""margin-bottom:35;\n""    border:none;\n""")
                                self.ui.motion_detector_6.setStyleSheet("\n""\n""\n""background-color: transparent;\n""    image: url(:/images/phptps/alarmha-19.svg);\n""")
                        else:
                                None         

                if self.door_alarm_status== True  :
                        if self.door_is_red :
                                
                                self.ui.coler_right_6.setStyleSheet("\n""    \n""    \n""    \n""    \n""image: url(:/images/images/phptps/alarm off-01.svg);\n""    background-repeat: none;\n""\n""\n""    border:none;\n""\n""")
                                self.ui.entray_detector_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    \n""    image: url(:/images/phptps/alarmha-21.svg);\n""\n""")
                                self.door_is_red=False
                                self.beep_alarm()
                        elif not self.door_is_red :
                                
                                self.ui.coler_right_6.setStyleSheet("\n""    \n""    \n""    \n""    \n""image: url(:/images/images/phptps/alarm on-01.svg);\n""    background-repeat: none;\n""\n""\n""    border:none;\n""\n""")
                                self.ui.entray_detector_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    \n""    image: url(:/images/phptps/alarmha-16.svg);\n""\n""")
                                self.door_is_red=True
                                self.beep_alarm()
                                
                elif not self.door_alarm_status :  
                        
                        if self.door_is_red :
                                self.door_is_red=False
                                self.ui.coler_right_6.setStyleSheet("\n""    \n""    \n""    \n""    \n""image: url(:/images/images/phptps/alarm off-01.svg);\n""    background-repeat: none;\n""\n""\n""    border:none;\n""\n""")
                                self.ui.entray_detector_3.setStyleSheet("\n""\n""    background-color: transparent;\n""    \n""    image: url(:/images/phptps/alarmha-21.svg);\n""\n""")
                        else:
                                None         


        def check_clients(self):
                server11 = Server()
                connected_clients = server11.get_connected_clients()
                if connected_clients:
                # اگر حداقل یک کلاینت وصل شده باشد، تغییرات مورد نظر در UI اعمال شود
                        self.change_connect_state_to_connect()
                elif (connected_clients == False) & (self.conection_status):
                        self.change_connect_state_to_disconnect()
        def change_connect_state_to_connect(self):
                self.conection_status=True
                
                self.ui.label_71.setStyleSheet("image: url(:/images/phptps/Icon Conect-01-01.svg);\n""")                
        def change_connect_state_to_disconnect(self):
                self.conection_status=False
                self.ui.label_71.setStyleSheet("image: url(:/images/phptps/Icon Diconect-01.svg);\n""")                
                               
                

#              
        
                
                
        def resizeEvent(self, event: QtGui.QResizeEvent):
            width = event.size().width()
            height = event.size().height()
            
        #     print(width)
        #     print(height)
            
            
            if ( (1050>width) & (664>height) ):
                self.ui.stackedWidget.setStyleSheet("font: 7pt;")
                self.font_center="5"
               
                self.font_adad_bala_paiin="15"
                self.font_adad_center="12"
                
                self.ui.label_99.setStyleSheet("\n"
                    "#label_99{\n"
                    "background-color:none;\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 5pt;\n"
                    "\n"
                    "}\n"
                    "")
                
                self.ui.label_103.setStyleSheet("\n"
                    "\n"
                    "#label_103{\n"
                    "background-color:none;\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 5pt;\n"
                    "\n"
                    "}\n"
                    "\n"
                    "\n"
                    "")
                
                
                
                
                
                self.ui.temp_down_40.setStyleSheet("#temp_down_40{\n"
                        "     color: white;\n"
                        "font: 15pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                
                self.ui.temp_down_41.setStyleSheet("#temp_down_41{\n"
                        "     color: white;\n"
                        "font: 15pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_33.setStyleSheet("#temp_down_33{\n"
                        "     color: white;\n"
                        "font: 15pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_34.setStyleSheet("#temp_down_34{\n"
                        "     color: white;\n"
                        "font: 15pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_35.setStyleSheet("#temp_down_35{\n"
                        "     color: white;\n"
                        "font: 15pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_49.setStyleSheet("#temp_down_49{\n"
                        "     color: white;\n"
                        "font: 15pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_45.setStyleSheet("#temp_down_45{\n"
                        "     color: white;\n"
                        "font: 15pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_51.setStyleSheet("#temp_down_51{\n"
                        "     color: white;\n"
                        "font: 15pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_46.setStyleSheet("#temp_down_46{\n"
                        "     color: white;\n"
                        "font: 15pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_47.setStyleSheet("#temp_down_47{\n"
                        "     color: white;\n"
                        "font: 15pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_52.setStyleSheet("#temp_down_52{\n"
                        "     color: white;\n"
                        "font: 12pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_53.setStyleSheet("#temp_down_53{\n"
                        "     color: white;\n"
                        "font: 12pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                
                self.ui.label_69.setStyleSheet("\n"
                        "#label_69{\n"
                        "color: rgb(255, 255, 255);\n"
                        "border:none;\n"
                        "font:24px\n"
                        "\n"
                        "}")
                self.ui.label_70.setStyleSheet("\n"
                        "#label_70{\n"
                        "color: rgb(255, 255, 255);\n"
                        "border:none;\n"
                        "font:23px\n"
                        "\n"
                        "}")
            
            
            if ( (1240>width > 1050) & (855>height > 664) ):
                # font=QtGui.QFont()
                # font.setPointSize(16)
                self.ui.stackedWidget.setStyleSheet("font: 10pt;")
                
                self.font_center="5"
              
                self.font_adad_bala_paiin="22"
                self.font_adad_center="22"
                
                
                self.ui.label_99.setStyleSheet("\n"
                    "#label_99{\n"
                    "background-color:none;\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 5pt;\n"
                    "\n"
                    "}\n"
                    "")
                
                self.ui.label_103.setStyleSheet("\n"
                    "\n"
                    "#label_103{\n"
                    "background-color:none;\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 5pt;\n"
                    "\n"
                    "}\n"
                    "\n"
                    "\n"
                    "")
                
                
                self.ui.temp_down_40.setStyleSheet("#temp_down_40{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                
                self.ui.temp_down_41.setStyleSheet("#temp_down_41{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_33.setStyleSheet("#temp_down_33{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_34.setStyleSheet("#temp_down_34{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_35.setStyleSheet("#temp_down_35{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_49.setStyleSheet("#temp_down_49{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_45.setStyleSheet("#temp_down_45{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_51.setStyleSheet("#temp_down_51{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_46.setStyleSheet("#temp_down_46{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_47.setStyleSheet("#temp_down_47{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_52.setStyleSheet("#temp_down_52{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_53.setStyleSheet("#temp_down_53{\n"
                        "     color: white;\n"
                        "       font:22px;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.label_69.setStyleSheet("\n"
                    "#label_69{\n"
                    "color: rgb(255, 255, 255);\n"
                    "border:none;\n"
                    "font:35px\n"
                    "\n"
                    "}")
                self.ui.label_70.setStyleSheet("\n"
                    "#label_70{\n"
                    "color: rgb(255, 255, 255);\n"
                    "border:none;\n"
                    "font:33px\n"
                    "\n"
                    "}")
                
                
                
                print("1")
            if( (1405>width > 1240) & (888>height > 855) ):
                # font=QtGui.QFont()
                # font.setPointSize(16)
                self.ui.stackedWidget.setStyleSheet("font: 14pt;")
                
                self.font_center="8"
              
                self.font_adad_bala_paiin="26"
                self.font_adad_center="26"
                
                self.ui.label_99.setStyleSheet("\n"
                    "#label_99{\n"
                    "background-color:none;\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 8pt;\n"
                    "\n"
                    "}\n"
                    "")
                
                self.ui.label_103.setStyleSheet("\n"
                    "\n"
                    "#label_103{\n"
                    "background-color:none;\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 8pt;\n"
                    "\n"
                    "}\n"
                    "\n"
                    "\n"
                    "")
                
                
                
                
                
                self.ui.temp_down_40.setStyleSheet("#temp_down_40{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                
                self.ui.temp_down_41.setStyleSheet("#temp_down_41{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_33.setStyleSheet("#temp_down_33{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_34.setStyleSheet("#temp_down_34{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_35.setStyleSheet("#temp_down_35{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_49.setStyleSheet("#temp_down_49{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_45.setStyleSheet("#temp_down_45{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_51.setStyleSheet("#temp_down_51{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_46.setStyleSheet("#temp_down_46{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_47.setStyleSheet("#temp_down_47{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_52.setStyleSheet("#temp_down_52{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_53.setStyleSheet("#temp_down_53{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                
                
                
                
                
                self.ui.label_69.setStyleSheet("\n"
                    "#label_69{\n"
                    "color: rgb(255, 255, 255);\n"
                    "border:none;\n"
                    "font:42px\n"
                    "\n"
                    "}")
                self.ui.label_70.setStyleSheet("\n"
                    "#label_70{\n"
                    "color: rgb(255, 255, 255);\n"
                    "border:none;\n"
                    "font:41px\n"
                    "\n"
                    "}")
                
                
                
                print("2")

            
            if( (width > 1405) & (height > 888) ):
                # font=QtGui.QFont()
                # font.setPointSize(16)
                self.ui.stackedWidget.setStyleSheet("font: 16pt;")
                
                                
                self.font_center="9"
              
                self.font_adad_bala_paiin="26"
                self.font_adad_center="26"
                
                self.ui.label_99.setStyleSheet("\n"
                    "#label_99{\n"
                    "background-color:none;\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 9pt;\n"
                    "\n"
                    "}\n"
                    "")
                
                self.ui.label_103.setStyleSheet("\n"
                    "\n"
                    "#label_103{\n"
                    "background-color:none;\n"
                    "color: rgb(255, 255, 255);\n"
                    "font: 9pt;\n"
                    "\n"
                    "}\n"
                    "\n"
                    "\n"
                    "")
                
                
                
                
                
                
                self.ui.temp_down_40.setStyleSheet("#temp_down_40{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                
                self.ui.temp_down_41.setStyleSheet("#temp_down_41{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_33.setStyleSheet("#temp_down_33{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_34.setStyleSheet("#temp_down_34{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_35.setStyleSheet("#temp_down_35{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_49.setStyleSheet("#temp_down_49{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_45.setStyleSheet("#temp_down_45{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_51.setStyleSheet("#temp_down_51{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_46.setStyleSheet("#temp_down_46{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_47.setStyleSheet("#temp_down_47{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_52.setStyleSheet("#temp_down_52{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                self.ui.temp_down_53.setStyleSheet("#temp_down_53{\n"
                        "     color: white;\n"
                        "font: 26pt;\n"
                        "\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                
                
                self.ui.label_69.setStyleSheet("\n"
                    "#label_69{\n"
                    "color: rgb(255, 255, 255);\n"
                    "border:none;\n"
                    "font:49px\n"
                    "\n"
                    "}")
                self.ui.label_70.setStyleSheet("\n"
                    "#label_70{\n"
                    "color: rgb(255, 255, 255);\n"
                    "border:none;\n"
                    "font:47px\n"
                    "\n"
                    "}")
                
                
                
                print("3")
            
            
            
            super().resizeEvent(event)
        
        

                
def start_server():
          
        server = Server()
        server.start_server()
        
        
def stop_server_thread():
        server = Server()
        server.start_server()
        app.quit() 
        
if __name__ == "__main__":
    import sys
    import time
    

    
    
    pc_ip.set_static_ip()
    time.sleep(3.2)
    print(get_local_IP())
    app = QtWidgets.QApplication(sys.argv)
    icon_path = QtGui.QPixmap("C:/Users/shayan/Desktop/conex_project - Copy/griffin_icon.ico")


    # ایجاد یک آیکون با استفاده از مسیر فایل تصویر
    icon = QtGui.QIcon(icon_path)

    # استفاده از آیکون برای برنامه
    app.setWindowIcon(icon)
    app.setApplicationDisplayName("Griffin")
    main_window = Mainwindow()
    
    thread = threading.Thread(target=start_server)
    thread.start()
    
    app.aboutToQuit.connect(stop_server_thread)
        

    sys.exit(app.exec_())