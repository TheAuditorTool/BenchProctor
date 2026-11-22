<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00224Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        [$data] = [$userInput, 'http'];
        ini_set('yaml.decode_php', '1');
        $document = yaml_parse((string)$data);
        return response()->json(['ok' => 1]);
    }
}
