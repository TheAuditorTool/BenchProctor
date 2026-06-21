# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest15080(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
