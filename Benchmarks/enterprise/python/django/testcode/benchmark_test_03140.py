# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import runpy


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest03140(request):
    field_value = UserForm(request.POST).data.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
