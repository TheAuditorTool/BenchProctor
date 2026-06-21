# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def normalise_input(value):
    return value.strip()

def BenchmarkTest45042(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = normalise_input(field_value)
    def _primary():
        return redirect(str(data))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
