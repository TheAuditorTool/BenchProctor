# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from django.shortcuts import redirect
import urllib.parse


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def normalise_input(value):
    return value.strip()

def BenchmarkTest49560(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = normalise_input(field_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
