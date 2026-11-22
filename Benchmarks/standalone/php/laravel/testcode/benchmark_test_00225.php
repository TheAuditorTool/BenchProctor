<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00225Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = vsprintf('%1$s', [$userInput]);
        \App\Models\User::where('id', $data)->get();
        return response()->json(['ok' => 1]);
    }
}
