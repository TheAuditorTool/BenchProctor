<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00094Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        session(['data' => (string) $data]);
        return response()->json(['ok' => 1]);
    }
}
