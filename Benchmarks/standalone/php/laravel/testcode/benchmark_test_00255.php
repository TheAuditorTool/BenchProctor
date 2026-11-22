<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00255Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $catalog = new \DOMDocument();
        $catalog->load('/var/app/data/catalog.xml');
        $item = $catalog->getElementById((string)$data);
        $price = $item->getAttribute('price');
        return response()->json(['ok' => 1]);
    }
}
