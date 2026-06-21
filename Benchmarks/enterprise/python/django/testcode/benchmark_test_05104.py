# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ldap
import re
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
request_state: dict[str, str] = {}

def BenchmarkTest05104(request):
    field_value = UserForm(request.POST).data.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return JsonResponse({"saved": True})
