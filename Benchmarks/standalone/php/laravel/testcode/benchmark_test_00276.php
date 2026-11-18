<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00276Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $_coerced = in_array(strtolower((string)$data), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        session(['data' => (string) $parsedBool]);
        return response()->json(['ok' => 1]);
    }
}
