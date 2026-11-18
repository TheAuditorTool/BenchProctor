<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00187Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->file('upload')?->getClientOriginalName() ?? '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
