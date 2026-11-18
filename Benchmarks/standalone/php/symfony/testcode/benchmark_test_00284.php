<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00284', methods: ['POST'])]
class BenchmarkTest00284Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        exec('tar -czf /tmp/backup.tgz ' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
