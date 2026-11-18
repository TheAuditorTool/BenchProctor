<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00071', methods: ['POST'])]
class BenchmarkTest00071Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        [$data] = [$userInput, 'http'];
        $_coerced = (float)$data;
        $processed = $_coerced;
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $processed . "']");
        return new JsonResponse(["committed" => true]);
    }
}
