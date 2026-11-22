<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00170', methods: ['POST'])]
class BenchmarkTest00170Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['variables']['input'] ?? '';
        $catalog = new \DOMDocument();
        $catalog->load('/var/app/data/catalog.xml');
        $item = $catalog->getElementById((string)$userInput);
        $price = $item->getAttribute('price');
        return new JsonResponse(["committed" => true]);
    }
}
