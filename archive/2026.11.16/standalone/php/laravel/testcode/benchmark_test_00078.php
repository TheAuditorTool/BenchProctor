<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00078Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $data = ($userInput !== null) ? $userInput : '';
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
