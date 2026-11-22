<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00103', methods: ['POST'])]
class BenchmarkTest00103Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $reader = new \XMLReader();
        $reader->XML((string)$data, null, LIBXML_NONET);
        $name = '';
        while ($reader->read()) {
            if ($reader->nodeType === \XMLReader::ELEMENT && $reader->name === 'name') { $name = $reader->readString(); }
        }
        return new JsonResponse(["committed" => true]);
    }
}
