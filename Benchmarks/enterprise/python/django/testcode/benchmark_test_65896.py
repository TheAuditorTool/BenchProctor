# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest65896(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % str(field_value)
    return redirect(str(data))
