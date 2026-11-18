<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00549', methods: ['POST'])]
class BenchmarkTest00549Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = vsprintf('%1$s', [$userInput]);
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return new JsonResponse(["committed" => true]);
    }
}
