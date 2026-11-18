# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00503(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    return redirect(str(data))
