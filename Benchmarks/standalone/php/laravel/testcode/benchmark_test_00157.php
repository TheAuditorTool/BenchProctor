<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00157Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $data = ($userInput !== null) ? $userInput : '';
        $quantity = (int) $data;
        $lineTotal = intval($quantity * 1999);
        return response()->json(['line_total_cents' => $lineTotal], 200);
    }
}
