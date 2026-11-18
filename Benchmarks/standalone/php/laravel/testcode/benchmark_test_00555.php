<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00555Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT bio FROM profiles LIMIT 1')->bio;
        DB::select('SELECT * FROM users WHERE id = \'' . $userInput . '\'');
        return response()->json(['ok' => 1]);
    }
}
