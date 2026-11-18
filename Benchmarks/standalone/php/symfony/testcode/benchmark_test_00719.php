<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00719', methods: ['POST'])]
class BenchmarkTest00719Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        (new \Symfony\Component\Yaml\Parser())->parse($userInput, \Symfony\Component\Yaml\Yaml::PARSE_OBJECT | \Symfony\Component\Yaml\Yaml::PARSE_OBJECT_FOR_MAP);
        return new JsonResponse(["committed" => true]);
    }
}
