<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00191Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $data = (!empty($userInput)) ? $userInput : '';
        eval((string)$data);
        return response()->json(['ok' => 1]);
    }
}
