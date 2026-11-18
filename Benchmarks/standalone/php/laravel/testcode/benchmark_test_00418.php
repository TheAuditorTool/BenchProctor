<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00418Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        system('gzip -f /var/app/reports/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
