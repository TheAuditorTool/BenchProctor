<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00024Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = str_replace("\0", '', $userInput);
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
