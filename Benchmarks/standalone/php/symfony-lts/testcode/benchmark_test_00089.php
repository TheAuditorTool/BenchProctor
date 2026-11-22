<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00089', methods: ['POST'])]
class BenchmarkTest00089Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        ini_set('yaml.decode_php', '0');
        $document = yaml_parse((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
