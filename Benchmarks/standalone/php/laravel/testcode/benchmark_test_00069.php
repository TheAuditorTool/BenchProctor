<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00069Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $content = file_get_contents('/var/app/data/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
