<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00115Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $data = sprintf('%s', $userInput);
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
