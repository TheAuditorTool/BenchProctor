<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00537Controller
{
    public function __invoke()
    {
        $userInput = config('app.value', '');
        $data = (!empty($userInput)) ? $userInput : '';
        DB::select('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return response()->json(['ok' => 1]);
    }
}
