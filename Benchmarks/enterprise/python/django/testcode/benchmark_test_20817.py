# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest20817(request):
    field_value = UserForm(request.POST).data.get('field', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(field_value),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
