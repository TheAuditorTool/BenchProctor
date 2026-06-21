# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from urllib.parse import unquote
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest56555(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
