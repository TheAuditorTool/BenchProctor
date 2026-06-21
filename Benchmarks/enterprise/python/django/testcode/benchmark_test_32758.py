# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from django.http import HttpResponse


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest32758(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(str(processed), content_type='text/html')
