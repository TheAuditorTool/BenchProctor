# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest08625(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ' '.join(str(field_value).split())
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return JsonResponse({"saved": True})
