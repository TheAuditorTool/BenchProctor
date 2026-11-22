<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00357Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        ini_set('yaml.decode_php', '0');
        $document = yaml_parse((string)$userInput);
        return response()->json(['ok' => 1]);
    }
}
