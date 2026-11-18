<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00072', methods: ['POST'])]
class BenchmarkTest00072Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        shell_exec('bash -c "grep -r ' . $data . ' /var/app/logs"');
        return new JsonResponse(["committed" => true]);
    }
}
