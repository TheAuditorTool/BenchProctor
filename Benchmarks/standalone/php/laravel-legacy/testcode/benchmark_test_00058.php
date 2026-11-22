<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00058Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $catalog = new \DOMDocument();
        $catalog->load('/var/app/data/catalog.xml');
        $item = $catalog->getElementById((string)$userInput);
        $price = $item->getAttribute('price');
        return response()->json(['ok' => 1]);
    }
}
