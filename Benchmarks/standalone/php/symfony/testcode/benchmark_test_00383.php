<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00383', methods: ['POST'])]
class BenchmarkTest00383Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = (!empty($userInput)) ? $userInput : '';
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return new JsonResponse(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        shell_exec('bash -c "grep -r ' . $allowedBin . ' /var/app/logs"');
        return new JsonResponse(["committed" => true]);
    }
}
