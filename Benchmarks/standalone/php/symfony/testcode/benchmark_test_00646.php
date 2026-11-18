<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00646', methods: ['POST'])]
class BenchmarkTest00646Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Origin', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $data . "']");
        return new JsonResponse(["committed" => true]);
    }
}
