<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00684', methods: ['POST'])]
class BenchmarkTest00684Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NOENT | LIBXML_DTDLOAD);
        return new JsonResponse(["committed" => true]);
    }
}
