# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest09458(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = field_value if field_value else 'default'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
