<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00189', methods: ['POST'])]
class BenchmarkTest00189Controller
{
    public function __invoke()
    {
        $userInput = (new \Redis())->get('user_data');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        ini_set('yaml.decode_php', '1');
        $document = yaml_parse((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
