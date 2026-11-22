<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00086', methods: ['POST'])]
class BenchmarkTest00086Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->files->get('upload')?->getClientOriginalName() ?? '');
        $data = (!empty($userInput)) ? $userInput : '';
        $catalog = new \DOMDocument();
        $catalog->load('/var/app/data/catalog.xml');
        $item = $catalog->getElementById((string)$data);
        if ($item === null) { return new JsonResponse(["error" => "not found"], 404); }
        $price = $item->getAttribute('price');
        return new JsonResponse(["committed" => true]);
    }
}
