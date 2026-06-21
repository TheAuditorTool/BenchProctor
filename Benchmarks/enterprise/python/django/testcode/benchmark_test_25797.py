# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def ensure_str(value):
    return str(value)

def BenchmarkTest25797(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ensure_str(field_value)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
