<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00455', methods: ['POST'])]
class BenchmarkTest00455Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return new JsonResponse(["committed" => true]);
    }
}
