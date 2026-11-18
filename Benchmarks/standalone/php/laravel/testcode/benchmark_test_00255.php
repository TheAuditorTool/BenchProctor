<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00255Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        if (!in_array((string)$userInput, ['config.json', 'index.html', 'readme.md'], true)) { return response()->json(['error' => 'forbidden'], 403); }
        $checkedPath = (string)$userInput;
        file_put_contents((string)$checkedPath, 'data');
        return response()->json(['ok' => 1]);
    }
}
