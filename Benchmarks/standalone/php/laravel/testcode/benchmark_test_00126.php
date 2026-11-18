<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00126Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $_coerced = in_array(strtolower((string)$data), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        session(['data' => (string) $parsedBool]);
        return response()->json(['ok' => 1]);
    }
}
