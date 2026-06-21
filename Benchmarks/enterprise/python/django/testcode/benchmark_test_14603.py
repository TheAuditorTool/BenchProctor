# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest14603(request):
    field_value = UserForm(request.POST).data.get('field', '')
    return redirect(str(field_value))
