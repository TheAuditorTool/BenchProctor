<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00273', methods: ['POST'])]
class BenchmarkTest00273Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = (!empty($userInput)) ? $userInput : '';
        $digest = md5((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
