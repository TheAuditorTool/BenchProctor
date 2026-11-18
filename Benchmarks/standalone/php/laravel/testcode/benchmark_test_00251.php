<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00251Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $checkedPath = '/var/app/data/' . basename($data);
        unlink((string)$checkedPath);
        return response()->json(['ok' => 1]);
    }
}
