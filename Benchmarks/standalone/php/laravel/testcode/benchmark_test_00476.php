<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00476Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $data = str_replace("\0", '', $userInput);
        return response()->json(['ok' => 1])->cookie('session', (string)$data, 0, '/', null, false, true, false, 'Strict');
    }
}
