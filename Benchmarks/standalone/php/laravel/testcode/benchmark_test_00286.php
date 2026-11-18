<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00286Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        return response()->json(['ok' => 1])->cookie('session', (string)$data, 0, '/', null, false, true, false, 'Strict');
    }
}
