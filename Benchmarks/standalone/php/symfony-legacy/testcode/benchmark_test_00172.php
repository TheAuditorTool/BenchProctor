<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00172', methods: ['POST'])]
class BenchmarkTest00172Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Host', '');
        $data = str_replace("\0", '', $userInput);
        if (!preg_match('#^[a-zA-Z0-9 _.\\-]+$#', $data)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $session = $request->getSession();
        $session->replace(array_merge($session->all(), ['data' => (string) $processed, 'data_updated_at' => time()]));
        return new JsonResponse(["committed" => true]);
    }
}
