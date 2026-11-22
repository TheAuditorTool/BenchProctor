<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00097Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = sprintf('%s', $userInput);
        $resolved = realpath('/var/app/data/' . $data);
        if ($resolved === false || strpos($resolved, '/var/app/data/') !== 0) { return response()->json(['error'=>'forbidden'], 403); }
        $checkedPath = $resolved;
        $content = file_get_contents($checkedPath);
        return response()->json(['ok' => 1]);
    }
}
