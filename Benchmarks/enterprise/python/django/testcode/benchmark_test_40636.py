# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest40636(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = field_value if field_value else 'default'
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
