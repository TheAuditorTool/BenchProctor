<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00300Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $content = file_get_contents('/var/app/data/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
