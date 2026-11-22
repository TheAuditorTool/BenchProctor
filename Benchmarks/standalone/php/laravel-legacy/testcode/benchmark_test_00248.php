<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00248Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $quantity = (int) $boundedVal;
        $lineTotal = intval($quantity * 1999);
        return response()->json(['line_total_cents' => $lineTotal], 200);
    }
}
