<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00498', methods: ['POST'])]
class BenchmarkTest00498Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return new JsonResponse(["committed" => true]);
    }
}
