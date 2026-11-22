<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00244', methods: ['POST'])]
class BenchmarkTest00244Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $data = vsprintf('%1$s', [$userInput]);
        $errno = 0; $errstr = '';
        fsockopen((string) parse_url((string)$data, PHP_URL_HOST), 80, $errno, $errstr, 30);
        return new JsonResponse(["committed" => true]);
    }
}
