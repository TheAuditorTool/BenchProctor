<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00556Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
