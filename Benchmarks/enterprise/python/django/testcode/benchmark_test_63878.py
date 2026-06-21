# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def to_text(value):
    return str(value).strip()

def BenchmarkTest63878(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = to_text(field_value)
    def _primary():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
