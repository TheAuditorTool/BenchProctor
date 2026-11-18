<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00609Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        system('gzip -f /var/app/reports/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
