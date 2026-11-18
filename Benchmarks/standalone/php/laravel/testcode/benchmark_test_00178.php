<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00178Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = ($userInput !== null) ? $userInput : '';
        $_coerced = (float)$data;
        $processed = $_coerced;
        session(['data' => (string) $processed]);
        return response()->json(['ok' => 1]);
    }
}
