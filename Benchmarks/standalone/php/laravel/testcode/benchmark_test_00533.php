<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00533Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->route('id') ?? $request->input('id', ''));
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        DB::select('SELECT * FROM users WHERE id = ?', [$data]);
        return response()->json(['ok' => 1]);
    }
}
