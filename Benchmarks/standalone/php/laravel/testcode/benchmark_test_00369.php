<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00369Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        file_get_contents((string)$data);
        return response()->json(['ok' => 1]);
    }
}
