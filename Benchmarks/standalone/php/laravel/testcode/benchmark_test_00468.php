<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00468Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = str_replace("\0", '', $userInput);
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
