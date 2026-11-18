<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00446', methods: ['POST'])]
class BenchmarkTest00446Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NOENT | LIBXML_DTDLOAD);
        return new JsonResponse(["committed" => true]);
    }
}
