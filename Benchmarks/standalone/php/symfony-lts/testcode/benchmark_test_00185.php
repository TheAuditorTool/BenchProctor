<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00185', methods: ['POST'])]
class BenchmarkTest00185Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        [$data] = [$userInput, 'http'];
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$data)) { error_log('enum validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $session = $request->getSession();
        $session->replace(array_merge($session->all(), ['data' => (string) $processed, 'data_updated_at' => time()]));
        return new JsonResponse(["committed" => true]);
    }
}
