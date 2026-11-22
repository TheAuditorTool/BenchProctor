<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00242', methods: ['POST'])]
class BenchmarkTest00242Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $email = $xpath->evaluate("string(//user[@id='" . $data . "']/email)");
        return new JsonResponse(["committed" => true]);
    }
}
