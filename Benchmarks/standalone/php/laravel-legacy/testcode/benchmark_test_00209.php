<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00209Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->route('id') ?? $request->input('id', ''));
        $data = sprintf('%s', $userInput);
        session(['data' => (string) $data]);
        return response()->json(['ok' => 1]);
    }
}
