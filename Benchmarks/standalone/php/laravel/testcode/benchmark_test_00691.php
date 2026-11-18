<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00691Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        return response()->json(['ok' => 1])->cookie('session', (string)$data, 0, '/', null, true, true, false, 'Strict');
    }
}
