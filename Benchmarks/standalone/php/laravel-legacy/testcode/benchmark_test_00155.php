<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00155Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $reader = new \XMLReader();
        $reader->XML((string)$data, null, LIBXML_NOENT | LIBXML_DTDLOAD);
        $name = '';
        while ($reader->read()) {
            if ($reader->nodeType === \XMLReader::ELEMENT && $reader->name === 'name') { $name = $reader->readString(); }
        }
        return response()->json(['ok' => 1]);
    }
}
