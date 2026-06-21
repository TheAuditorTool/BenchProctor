# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def ensure_str(value):
    return str(value)

def BenchmarkTest20049(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ensure_str(field_value)
    processed = data[:64]
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
