<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00304Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $reader = new \XMLReader();
        $reader->XML((string)$data, null, LIBXML_NONET);
        $name = '';
        while ($reader->read()) {
            if ($reader->nodeType === \XMLReader::ELEMENT && $reader->name === 'name') { $name = $reader->readString(); }
        }
        return response()->json(['ok' => 1]);
    }
}
