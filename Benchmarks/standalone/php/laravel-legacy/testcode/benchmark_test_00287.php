<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00287Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        \Illuminate\Support\Facades\Session::put(['data' => (string) $data, 'data_updated_at' => time()]);
        return response()->json(['ok' => 1]);
    }
}
