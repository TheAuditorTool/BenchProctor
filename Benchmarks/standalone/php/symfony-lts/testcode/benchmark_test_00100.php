<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00100', methods: ['POST'])]
class BenchmarkTest00100Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $_prefix = strtolower(substr($userInput, 0, 1));
        $data = '';
        switch ($_prefix) {
            case 'h': $data = strtolower($userInput); break;
            case 'f': $data = strtoupper($userInput); break;
            default: $data = trim($userInput); break;
        }
        $session = $request->getSession();
        $session->replace(array_merge($session->all(), ['data' => (string) $data, 'data_updated_at' => time()]));
        return new JsonResponse(["committed" => true]);
    }
}
