<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00071Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
