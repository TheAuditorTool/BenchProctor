<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00247Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $quantity = (int) $boundedVal;
        $lineTotal = intval($quantity * 1999);
        return response()->json(['line_total_cents' => $lineTotal], 200);
    }
}
