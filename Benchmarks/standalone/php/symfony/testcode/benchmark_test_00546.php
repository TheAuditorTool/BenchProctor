<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00546', methods: ['POST'])]
class BenchmarkTest00546Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        (new \Symfony\Component\Yaml\Parser())->parse($userInput, \Symfony\Component\Yaml\Yaml::PARSE_OBJECT | \Symfony\Component\Yaml\Yaml::PARSE_OBJECT_FOR_MAP);
        return new JsonResponse(["committed" => true]);
    }
}
