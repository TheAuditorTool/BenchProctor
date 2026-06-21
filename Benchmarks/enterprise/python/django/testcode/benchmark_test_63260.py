# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest63260(request):
    field_value = UserForm(request.POST).data.get('field', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(field_value))
    return JsonResponse({"saved": True})
