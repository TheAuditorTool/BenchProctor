# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def to_text(value):
    return str(value).strip()

def BenchmarkTest05894(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = to_text(field_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
