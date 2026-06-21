# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest13764(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = field_value if field_value else 'default'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
