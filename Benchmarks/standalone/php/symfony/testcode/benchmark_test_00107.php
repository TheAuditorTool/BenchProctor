<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00107', methods: ['POST'])]
class BenchmarkTest00107Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        (new \Symfony\Component\Yaml\Parser())->parse($data, \Symfony\Component\Yaml\Yaml::PARSE_OBJECT | \Symfony\Component\Yaml\Yaml::PARSE_OBJECT_FOR_MAP);
        return new JsonResponse(["committed" => true]);
    }
}
