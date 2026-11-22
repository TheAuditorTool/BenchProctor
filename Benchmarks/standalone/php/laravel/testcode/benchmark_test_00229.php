<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00229Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        [$data] = [$userInput, 'http'];
        $catalog = new \DOMDocument();
        $catalog->load('/var/app/data/catalog.xml');
        $item = $catalog->getElementById((string)$data);
        if ($item === null) { return response()->json(["error" => "not found"], 404); }
        $price = $item->getAttribute('price');
        return response()->json(['ok' => 1]);
    }
}
