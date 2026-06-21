# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest69911(request):
    field_value = UserForm(request.POST).data.get('field', '')
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
