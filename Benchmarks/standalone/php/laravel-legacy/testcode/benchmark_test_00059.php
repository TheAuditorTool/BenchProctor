<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00059Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        session(['data' => (string) $data]);
        return response()->json(['ok' => 1]);
    }
}
