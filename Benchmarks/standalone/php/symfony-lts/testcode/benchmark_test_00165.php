<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00165', methods: ['POST'])]
class BenchmarkTest00165Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $catalog = new \DOMDocument();
        $catalog->load('/var/app/data/catalog.xml');
        $item = $catalog->getElementById((string)$data);
        $price = $item->getAttribute('price');
        return new JsonResponse(["committed" => true]);
    }
}
