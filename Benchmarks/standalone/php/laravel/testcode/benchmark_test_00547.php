<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00547Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->route('id') ?? $request->input('id', ''));
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $result = DB::table('users')->where('id', $data)->first();
        $value = $result->name;
        return response()->json(['ok' => 1]);
    }
}
