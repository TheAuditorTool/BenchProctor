# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest78247(request):
    field_value = UserForm(request.POST).data.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
