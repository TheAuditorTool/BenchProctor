<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00082', methods: ['POST'])]
class BenchmarkTest00082Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = ($userInput !== null) ? $userInput : '';
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return new JsonResponse(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        shell_exec('bash -c "grep -r ' . $allowedBin . ' /var/app/logs"');
        return new JsonResponse(["committed" => true]);
    }
}
