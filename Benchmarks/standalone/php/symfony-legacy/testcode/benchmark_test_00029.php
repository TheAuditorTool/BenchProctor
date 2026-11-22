<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00029', methods: ['POST'])]
class BenchmarkTest00029Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $data = json_decode($userInput, true)['value'] ?? '';
        \Symfony\Component\Yaml\Yaml::parse((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
