<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00016', methods: ['POST'])]
class BenchmarkTest00016Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        [$data] = [$userInput, 'http'];
        shell_exec('bash -c "grep -r ' . $data . ' /var/app/logs"');
        return new JsonResponse(["committed" => true]);
    }
}
