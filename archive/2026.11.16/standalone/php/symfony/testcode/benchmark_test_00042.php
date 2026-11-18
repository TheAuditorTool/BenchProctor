<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00042', methods: ['POST'])]
class BenchmarkTest00042Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $data = (!empty($userInput)) ? $userInput : '';
        mt_srand(ctype_digit((string)$data) ? (int)$data : 42);
        $token = mt_rand();
        return new JsonResponse(['token' => (string)$token], 200);
    }
}
