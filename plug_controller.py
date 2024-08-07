import os
from dotenv import load_dotenv, find_dotenv
from PyP100 import PyP110

load_dotenv(find_dotenv())

# SETUP
plug_ip = os.environ.get("TAPO_IP")
plug_mail = os.environ.get("TAPO_MAIL")
plug_pwd = os.environ.get("TAPO_PWD")

p110 = PyP110.P110(f"{plug_ip}", f"{plug_mail}", f"{plug_pwd}")
# p110.handshake()
# p110.login()

def toggle_plug():
    p110.toggleState()

# usage = p110.getEnergyUsage()
# name = p110.getDeviceName()
# info = p110.getDeviceInfo()
# print(f"USAGE\n{usage}\n")
# print(f"name: {name}\n")
# print(f"info: {info}\n")
