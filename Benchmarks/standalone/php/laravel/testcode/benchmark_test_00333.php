<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00333Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        file_get_contents((string)$data);
        return response()->json(['ok' => 1]);
    }
}
