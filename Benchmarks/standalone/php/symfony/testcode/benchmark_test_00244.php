<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00244', methods: ['POST'])]
class BenchmarkTest00244Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = vsprintf('%1$s', [$userInput]);
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $data . "']");
        return new JsonResponse(["committed" => true]);
    }
}
