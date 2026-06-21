# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest30599(request):
    field_value = UserForm(request.POST).data.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
