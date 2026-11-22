<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00287Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        \Illuminate\Support\Facades\Cache::forever('tenant:display_name', (string) $data);
        return response()->json(['ok' => 1]);
    }
}
