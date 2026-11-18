<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00412', methods: ['POST'])]
class BenchmarkTest00412Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return new JsonResponse(["committed" => true]);
    }
}
