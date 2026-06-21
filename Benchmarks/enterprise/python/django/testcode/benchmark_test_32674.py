# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest32674(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = f'{field_value:.200s}'
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return JsonResponse({"saved": True})
