<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00543', methods: ['POST'])]
class BenchmarkTest00543Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $data = (!empty($userInput)) ? $userInput : '';
        if (!preg_match('#^[a-zA-Z0-9 _.%\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        exec('tar -czf /tmp/backup.tgz ' . (string)$processed);
        return new JsonResponse(["committed" => true]);
    }
}
