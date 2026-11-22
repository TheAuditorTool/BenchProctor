<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00208Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $quantity = (int) $data;
        $lineTotal = intval($quantity * 1999);
        return response()->json(['line_total_cents' => $lineTotal], 200);
    }
}
