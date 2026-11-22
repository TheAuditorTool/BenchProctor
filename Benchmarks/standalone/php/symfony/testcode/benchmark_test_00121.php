<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00121', methods: ['POST'])]
class BenchmarkTest00121Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $reader = new \XMLReader();
        $reader->XML((string)$data, null, LIBXML_NOENT | LIBXML_DTDLOAD);
        $name = '';
        while ($reader->read()) {
            if ($reader->nodeType === \XMLReader::ELEMENT && $reader->name === 'name') { $name = $reader->readString(); }
        }
        return new JsonResponse(["committed" => true]);
    }
}
