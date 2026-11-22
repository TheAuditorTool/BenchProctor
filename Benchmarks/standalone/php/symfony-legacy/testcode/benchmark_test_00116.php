<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00116', methods: ['POST'])]
class BenchmarkTest00116Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        [$data] = [$userInput, 'http'];
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return new JsonResponse(["committed" => true]);
    }
}
