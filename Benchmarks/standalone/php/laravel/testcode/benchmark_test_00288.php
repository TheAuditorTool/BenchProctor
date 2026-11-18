<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00288Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        if (!in_array((string)$data, ['config.json', 'index.html', 'readme.md'], true)) { return response()->json(['error' => 'forbidden'], 403); }
        $checkedPath = (string)$data;
        file_put_contents((string)$checkedPath, 'data');
        return response()->json(['ok' => 1]);
    }
}
