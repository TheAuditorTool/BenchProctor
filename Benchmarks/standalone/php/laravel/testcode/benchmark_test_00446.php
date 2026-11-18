<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00446Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT bio FROM profiles LIMIT 1')->bio;
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        DB::select('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return response()->json(['ok' => 1]);
    }
}
