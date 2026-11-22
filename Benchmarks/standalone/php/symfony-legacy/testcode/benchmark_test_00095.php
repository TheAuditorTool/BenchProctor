<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00095', methods: ['POST'])]
class BenchmarkTest00095Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Origin', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        \Symfony\Component\Yaml\Yaml::parse((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
