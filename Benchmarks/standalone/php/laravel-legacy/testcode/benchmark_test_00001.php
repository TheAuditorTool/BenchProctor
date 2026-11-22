<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00001Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        file_get_contents((string)$data);
        return response()->json(['ok' => 1]);
    }
}
