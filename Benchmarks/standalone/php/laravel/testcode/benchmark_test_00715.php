<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00715Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $checkedPath = '/var/app/data/' . basename($data);
        file_put_contents((string)$checkedPath, 'data');
        return response()->json(['ok' => 1]);
    }
}
