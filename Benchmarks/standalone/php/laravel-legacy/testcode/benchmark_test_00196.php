<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00196Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = "{$userInput}";
        \Illuminate\Support\Facades\Cache::forever('tenant:display_name', (string) $data);
        return response()->json(['ok' => 1]);
    }
}
