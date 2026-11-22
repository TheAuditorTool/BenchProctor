<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00040Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        [$data] = [$userInput, 'http'];
        file_put_contents('/var/uploads/' . $data, 'data');
        return response()->json(['ok' => 1]);
    }
}
