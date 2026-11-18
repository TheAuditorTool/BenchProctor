<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00483Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
