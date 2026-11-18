<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00174Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $data = (!empty($userInput)) ? $userInput : '';
        return response()->json(['ok' => 1])->cookie('session', (string)$data, 0, '/', null, true, true, false, 'Strict');
    }
}
