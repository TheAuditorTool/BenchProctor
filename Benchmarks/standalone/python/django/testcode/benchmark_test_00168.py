# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00168(request):
    multipart_value = request.POST.get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return redirect(str(data))
