<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00062Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('/tmp/data');
        DB::select('SELECT * FROM users WHERE id = ?', [$userInput]);
        return response()->json(['ok' => 1]);
    }
}
