# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def to_text(value):
    return str(value).strip()

def BenchmarkTest25880(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = to_text(field_value)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
