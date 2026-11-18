<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00474Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        \App\Models\User::where('id', $data)->get();
        return response()->json(['ok' => 1]);
    }
}
