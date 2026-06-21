# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
_shared_counter_lock = threading.Lock()

def BenchmarkTest75612(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = str(field_value).replace('\x00', '')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
