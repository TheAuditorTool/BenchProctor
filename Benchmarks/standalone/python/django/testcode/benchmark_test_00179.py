# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00179(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return redirect(str(data))
