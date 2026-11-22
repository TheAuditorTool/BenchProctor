<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00333Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        DB::select('SELECT * FROM users WHERE id = ?', [$data]);
        return response()->json(['ok' => 1]);
    }
}
