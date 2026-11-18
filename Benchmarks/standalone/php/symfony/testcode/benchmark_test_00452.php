<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00452', methods: ['POST'])]
class BenchmarkTest00452Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $data = ($userInput !== null) ? $userInput : '';
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
