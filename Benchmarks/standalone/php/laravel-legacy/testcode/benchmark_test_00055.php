<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00055Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $rows = DB::table('users')->whereRaw('id = \'' . $data . '\'')->get();
        return response()->json(['ok' => 1]);
    }
}
