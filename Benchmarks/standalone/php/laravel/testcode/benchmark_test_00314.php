<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00314Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = mb_convert_encoding($userInput, 'UTF-8');
        return response()->json(['ok' => 1])->cookie('session', (string)$data, 0, '/', null, false, true, false, 'Strict');
    }
}
