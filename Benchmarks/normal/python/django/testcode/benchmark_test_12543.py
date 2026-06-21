# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms
from app_runtime import auth_check


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest12543(request):
    field_value = UserForm(request.POST).data.get('field', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(field_value), store_cred)
    return JsonResponse({"saved": True})
