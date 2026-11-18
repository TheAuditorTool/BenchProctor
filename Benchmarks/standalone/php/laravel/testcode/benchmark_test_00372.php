<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00372Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT bio FROM profiles LIMIT 1')->bio;
        $data = (!empty($userInput)) ? $userInput : '';
        DB::select('SELECT * FROM users WHERE "' . str_replace('"', '""', (string)$data) . '" = 1');
        return response()->json(['ok' => 1]);
    }
}
