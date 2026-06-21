# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from dataclasses import dataclass
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
@dataclass
class FormData:
    payload: str

def BenchmarkTest18013(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = FormData(payload=field_value).payload
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
