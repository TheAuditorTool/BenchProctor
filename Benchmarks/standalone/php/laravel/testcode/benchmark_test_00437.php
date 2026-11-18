<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00437Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $data = ($userInput !== null) ? $userInput : '';
        $resolved = realpath('/var/app/data/' . $data);
        if ($resolved === false || strpos($resolved, '/var/app/data/') !== 0) { return response()->json(['error'=>'forbidden'], 403); }
        $checkedPath = $resolved;
        unlink((string)$checkedPath);
        return response()->json(['ok' => 1]);
    }
}
