<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00342Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        file_put_contents('/var/uploads/' . $data, 'data');
        return response()->json(['ok' => 1]);
    }
}
