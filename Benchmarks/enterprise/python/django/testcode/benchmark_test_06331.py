# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
_shared_counter_lock = threading.Lock()

def BenchmarkTest06331(request):
    field_value = UserForm(request.POST).data.get('field', '')
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
