<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00228', methods: ['POST'])]
class BenchmarkTest00228Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $doc = new \DOMDocument();
        $doc->loadXML((string)$userInput, LIBXML_NOENT | LIBXML_DTDLOAD);
        $name = $doc->getElementsByTagName('name')->item(0)?->textContent;
        return new JsonResponse(["committed" => true]);
    }
}
