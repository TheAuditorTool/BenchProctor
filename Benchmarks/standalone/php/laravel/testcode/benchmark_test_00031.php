<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00031Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        if (!in_array((string)$data, ['config.json', 'index.html', 'readme.md'], true)) { return response()->json(['error' => 'forbidden'], 403); }
        $checkedPath = (string)$data;
        unlink((string)$checkedPath);
        return response()->json(['ok' => 1]);
    }
}
