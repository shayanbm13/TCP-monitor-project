import json



def data_coder(temp1 , hum1 ,temp2,hum2,temp3,temp4,phonenum1,phonenum2,phonenum3 ,hour,minute):
    
    data = {
        "temp1": temp1,
        "hum1" : hum1,
        "temp2": temp2,
        "hum2" : hum2,
        "temp3": temp3,
        "temp4" : temp4,
        "phonenum1": phonenum1,
        "phonenum2" : phonenum2,
        "phonenum3": phonenum3 ,
        "hour": hour , 
        "minute": minute ,
        }
    
    json_data = json.dumps(data)
    return json_data

def data_decoder(jason_data):
    data = json.loads(jason_data)
    return data

def split_light(split_status,light_status):
    data = {
        "split": split_status,
        "light" : light_status,
        
        }
    json_data = json.dumps(data)
    return json_data


# a= [{
#                 phase1:       0,
#                 "phase2":       0,
#                 "phase3":       0,
#                 "generator":    0,
#                 "smoke":        0,
#                 "door": 0,
#                 "motion":       0,
#                 "voltage1":     220,
#                 "voltage2":     220,
#                 "voltage3":     220,
#                 "current1":     12,
#                 "current2":     10,
#                 "current3":     30,
#                 "split_current":        25,
#                 "current_temp1":        26,
#                 "set_temp1":    0,
#                 "current_hum1": 32,
#                 "set_hum1":     22,
#                 "current_temp2":        25,
#                 "set_temp2":    25,
#                 "current_hum2": 30,
#                 "set_hum2":     25,
#                 "current_temp3":        25,
#                 "set_temp3":    25,
#                 "current_temp4":        25,
#                 "set_temp4":    25,
#                 "light":        0,
#                 "split":        0
#         }]
# # a=str(a)

def msg_convertor(text):
    parts = text.split(",") 
    print(parts)
    values = {}
    for part in parts:
        # جدا کردن هر قسمت به نام و مقدار
        key_value = part.split(":")
        # حذف فاصله از هر بخش
        key = key_value[0].strip()
        value = int(key_value[1].strip())
        # قرار دادن مقدار در دیکشنری
        values[key] = value
    
    return values
        
# text = "phase1: 0,phase2: 0,phase3: 0,generator: 0,smoke: 0,door: 0,motion: 0,voltage1: 220,voltage2: 220,voltage3: 220,current1: 12,current2: 10,current3: 30,split_current: 25,current_temp1: 27,set_temp1: 26,current_hum1: 36,set_hum1: 30,current_temp2: 25,set_temp2: 30,current_hum2: 25,set_hum2: 30,current_temp3: 25,set_temp3: 30,current_temp4: 25,set_temp4: 30,light: 0,split: 0"
# # "phase1: 0,phase2: 0,phase3: 0,generator: 0,smoke: 0,door: 0"

# # # جدا کردن رشته بر اساس کاما برای جدا کردن اجزای مختلف
# # parts = text.split(",") 
# # print (parts)
# # # ایجاد یک دیکشنری برای نگهداری مقادیر
# # values = {}
# # for part in parts:
# #     # جدا کردن هر قسمت به نام و مقدار
# #     key_value = part.split(":")
# #     # حذف فاصله از هر بخش
# #     key = key_value[0].strip()
# #     value = key_value[1].strip()
# #     # قرار دادن مقدار در دیکشنری
# #     values[key] = value

# # # چاپ مقادیر موجود در دیکشنری
# values=msg_convertor(text)
# print(values["phase1"])
