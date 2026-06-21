# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest02334(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = field_value if field_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
