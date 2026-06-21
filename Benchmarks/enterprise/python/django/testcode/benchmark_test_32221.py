# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import ast
import runpy


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest32221(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    def _primary():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
