import pywhatkit
import inspect
#import scrapingAPKT04 as apkt
import pandas as pd
import pyautogui

#pywhatkit.sendwhatmsg_instantly(
#    phone_no = "<+6285376302378>",
#    message = "Hai, pesan ini dikirim melalui pywhatkit",
#)

df = pd.read_excel("output.xlsx")
print(df)

for i in range(0, df.shape[0]):

    sendText = (
        f"Yth. Bpk/Ibu berikut disampaikan keluhan dengan durasi melebihi 1 jam, agar dapat ditindaklanjuti\n\nNo. Lapor : {df.loc[i].at['No. Lapor']}\nStatus : {df.loc[i].at['Status ']} \nTipe Isu : {df.loc[i].at['Tipe Isu']}\nUnit : {df.loc[i].at['Unit']}\nNama : {df.loc[i].at['Nama']}\nTelp : {df.loc[i].at['No.Telepon']} \n\nPermasalahan : {df.loc[i].at['Permasalahan']} \n\nTanggal Buat : {df.loc[i].at['Tanggal Buat']} \nDurasi : {df.loc[i].at['Durasi']} \n\nTerima kasih \n\n Pesan dikirim melalui MRRC System"
     
    )
    

    pywhatkit.sendwhatmsg_to_group_instantly(
        "Ez3URazj2qi4pNFKjWiQwl",
        sendText,
    )
    #pyautogui.click(1050, 950)

#Test otomasi
#https://chat.whatsapp.com/KDxk4aAoJG4Cq9TjFZHWhW

#WADAU SISTEM
#https://chat.whatsapp.com/KsdLCcTShr4C3jpWygoycl


#Group APKT
#https://chat.whatsapp.com/Ez3URazj2qi4pNFKjWiQwl

#src = inspect.getsource(pywhatkit)
#print(src)