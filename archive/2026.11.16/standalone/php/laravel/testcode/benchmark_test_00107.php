<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00107Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $data = str_replace("\0", '', $userInput);
        eval((string)$data);
        return response()->json(['ok' => 1]);
    }
}
