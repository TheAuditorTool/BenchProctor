<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00594Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = urldecode($userInput);
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
