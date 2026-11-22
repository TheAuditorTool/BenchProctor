<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00176', methods: ['POST'])]
class BenchmarkTest00176Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = sprintf('%s', $userInput);
        $_coerced = in_array(strtolower((string)$data), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        $session = $request->getSession();
        $session->replace(array_merge($session->all(), ['data' => (string) $parsedBool, 'data_updated_at' => time()]));
        return new JsonResponse(["committed" => true]);
    }
}
