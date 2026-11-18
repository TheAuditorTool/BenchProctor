<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00567Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $_coerced = (float)$data;
        $processed = $_coerced;
        eval((string)$processed);
        return response()->json(['ok' => 1]);
    }
}
