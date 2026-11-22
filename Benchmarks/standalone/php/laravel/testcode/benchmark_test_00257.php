<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00257Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $data = "{$userInput}";
        \Illuminate\Support\Facades\Cache::forever('tenant:display_name', (string) $data);
        return response()->json(['ok' => 1]);
    }
}
