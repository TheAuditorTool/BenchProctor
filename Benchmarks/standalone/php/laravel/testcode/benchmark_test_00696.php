<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00696Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $data = (!empty($userInput)) ? $userInput : '';
        DB::select('SELECT * FROM users WHERE "' . str_replace('"', '""', (string)$data) . '" = 1');
        return response()->json(['ok' => 1]);
    }
}
