<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00296Controller
{
    public function __invoke()
    {
        $userInput = \Illuminate\Support\Facades\Redis::get('user_data');
        $data = str_replace("\0", '', $userInput);
        DB::select('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return response()->json(['ok' => 1]);
    }
}
