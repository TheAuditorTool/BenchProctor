<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00300Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        json_decode($userInput, true);
        return response()->json(['ok' => 1]);
    }
}
