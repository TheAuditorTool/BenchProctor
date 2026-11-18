<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00504Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
