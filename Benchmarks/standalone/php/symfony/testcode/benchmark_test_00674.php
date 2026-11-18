<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00674', methods: ['POST'])]
class BenchmarkTest00674Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        shell_exec('bash -c "grep -r ' . $data . ' /var/app/logs"');
        return new JsonResponse(["committed" => true]);
    }
}
