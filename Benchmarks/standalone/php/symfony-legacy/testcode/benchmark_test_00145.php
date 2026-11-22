<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00145', methods: ['POST'])]
class BenchmarkTest00145Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = base64_decode($userInput);
        $doc = new \DOMDocument();
        $doc->loadXML((string)$data, LIBXML_NOENT | LIBXML_DTDLOAD);
        $name = $doc->getElementsByTagName('name')->item(0)?->textContent;
        return new JsonResponse(["committed" => true]);
    }
}
