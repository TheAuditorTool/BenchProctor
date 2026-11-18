<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00627', methods: ['POST'])]
class BenchmarkTest00627Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $doc = new \DOMDocument();
        @$doc->load('/var/app/data/users.xml');
        $xpath = new \DOMXPath($doc);
        $nodes = $xpath->query("//user[@id='" . $data . "']");
        return new JsonResponse(["committed" => true]);
    }
}
