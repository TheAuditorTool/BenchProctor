<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00044Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $digest = hash('sha256', (string)$data);
        return response()->json(['ok' => 1]);
    }
}
