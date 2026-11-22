<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00211', methods: ['POST'])]
class BenchmarkTest00211Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $doc = new \DOMDocument();
        $doc->loadXML((string)$data, LIBXML_NONET);
        $name = $doc->getElementsByTagName('name')->item(0)?->textContent;
        return new JsonResponse(["committed" => true]);
    }
}
