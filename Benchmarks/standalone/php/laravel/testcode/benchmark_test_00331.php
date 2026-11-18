<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00331Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        return response()->json(['ok' => 1])->cookie('session', (string)$data, 0, '/', null, false, true, false, 'Strict');
    }
}
