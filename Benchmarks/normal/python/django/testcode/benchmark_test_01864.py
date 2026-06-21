# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from django import forms
from app_runtime import auth_check


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest01864(request):
    field_value = UserForm(request.POST).data.get('field', '')
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
