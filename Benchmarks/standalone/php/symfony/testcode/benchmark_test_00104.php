<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00104', methods: ['POST'])]
class BenchmarkTest00104Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $data = ($userInput !== null) ? $userInput : '';
        \Symfony\Component\Yaml\Yaml::parse((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
