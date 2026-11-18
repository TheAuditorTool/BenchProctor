<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00443Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        [$data] = [$userInput, 'http'];
        $checkedPath = '/var/app/data/' . basename($data);
        file_put_contents((string)$checkedPath, 'data');
        return response()->json(['ok' => 1]);
    }
}
