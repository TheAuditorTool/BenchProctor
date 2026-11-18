<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00509Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $data = vsprintf('%1$s', [$userInput]);
        eval((string)$data);
        return response()->json(['ok' => 1]);
    }
}
