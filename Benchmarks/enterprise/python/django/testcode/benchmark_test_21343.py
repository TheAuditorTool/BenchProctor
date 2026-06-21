# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import boto3
from django import forms
import os
import time


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest21343(request):
    field_value = UserForm(request.POST).data.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    key_expires_at = 4102444800
    active_key = store_cred if key_expires_at > int(time.time()) else os.environ['DATA_ENC_KEY_CURRENT']
    Fernet(active_key.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
