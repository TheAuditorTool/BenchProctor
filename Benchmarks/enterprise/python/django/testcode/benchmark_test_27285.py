# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def ensure_str(value):
    return str(value)

def BenchmarkTest27285(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ensure_str(field_value)
    processed = data[:64]
    random.seed(int(processed) if str(processed).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
