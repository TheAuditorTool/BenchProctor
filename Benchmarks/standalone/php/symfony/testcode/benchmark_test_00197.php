<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00197', methods: ['POST'])]
class BenchmarkTest00197Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Host', '');
        ini_set('yaml.decode_php', '0');
        $document = yaml_parse((string)$userInput);
        return new JsonResponse(["committed" => true]);
    }
}
