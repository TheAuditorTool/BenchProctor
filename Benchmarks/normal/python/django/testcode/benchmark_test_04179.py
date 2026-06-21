# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest04179(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % (field_value,)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
