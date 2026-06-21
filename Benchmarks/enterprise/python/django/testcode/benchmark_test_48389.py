# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest48389(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = default_blank(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
