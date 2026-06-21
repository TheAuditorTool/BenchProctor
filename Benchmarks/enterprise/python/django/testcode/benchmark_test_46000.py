# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
request_state: dict[str, str] = {}

def BenchmarkTest46000(request):
    field_value = UserForm(request.POST).data.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    processed = html.escape(data)
    return HttpResponse(mark_safe('<img src="' + str(processed) + '">'))
