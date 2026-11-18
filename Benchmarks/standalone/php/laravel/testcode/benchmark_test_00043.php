<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00043Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = "{$userInput}";
        DB::select('SELECT * FROM users WHERE "' . str_replace('"', '""', (string)$data) . '" = 1');
        return response()->json(['ok' => 1]);
    }
}
