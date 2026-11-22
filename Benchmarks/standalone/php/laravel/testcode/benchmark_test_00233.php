<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00233Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $data = (!empty($userInput)) ? $userInput : '';
        $digest = sha1((string)$data);
        return response()->json(['ok' => 1]);
    }
}
