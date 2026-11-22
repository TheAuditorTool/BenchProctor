<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00223', methods: ['POST'])]
class BenchmarkTest00223Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        if (!preg_match('#^[a-zA-Z0-9 _.%\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        shell_exec('bash -c "grep -r ' . $processed . ' /var/app/logs"');
        return new JsonResponse(["committed" => true]);
    }
}
