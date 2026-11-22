<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00142Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        file_get_contents((string)$data);
        return response()->json(['ok' => 1]);
    }
}
