# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from django.shortcuts import redirect
import urllib.parse


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest64123(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
