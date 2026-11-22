<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00304Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $reader = new \XMLReader();
        $reader->XML((string)$data, null, LIBXML_NOENT | LIBXML_DTDLOAD);
        $name = '';
        while ($reader->read()) {
            if ($reader->nodeType === \XMLReader::ELEMENT && $reader->name === 'name') { $name = $reader->readString(); }
        }
        return response()->json(['ok' => 1]);
    }
}
