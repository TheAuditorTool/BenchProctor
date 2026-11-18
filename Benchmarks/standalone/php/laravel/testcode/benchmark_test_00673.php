<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00673Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->file('upload')?->getClientOriginalName() ?? '');
        $data = ($userInput !== null) ? $userInput : '';
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
