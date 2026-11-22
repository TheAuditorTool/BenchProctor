<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00006', methods: ['POST'])]
class BenchmarkTest00006Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $errno = 0; $errstr = '';
        fsockopen((string) parse_url((string)$data, PHP_URL_HOST), 80, $errno, $errstr, 30);
        return new JsonResponse(["committed" => true]);
    }
}
