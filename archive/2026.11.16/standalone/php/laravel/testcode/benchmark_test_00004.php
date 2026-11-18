<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00004Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = vsprintf('%1$s', [$userInput]);
        DB::select('SELECT * FROM users WHERE id = \'' . $data . '\'');
        return response()->json(['ok' => 1]);
    }
}
