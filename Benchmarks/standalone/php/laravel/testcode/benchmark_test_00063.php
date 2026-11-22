<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00063Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $data = ($userInput !== null) ? $userInput : '';
        $pipes = [];
        proc_open(['echo', (string)$data], [], $pipes);
        return response()->json(['ok' => 1]);
    }
}
