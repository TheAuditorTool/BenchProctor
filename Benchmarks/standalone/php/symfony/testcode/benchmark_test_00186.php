<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\ORM\EntityManagerInterface;

#[Route('/BenchmarkTest00186', methods: ['POST'])]
class BenchmarkTest00186Controller
{
    public function __invoke(Request $request, EntityManagerInterface $em)
    {
        $userInput = $request->headers->get('User-Agent', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $em->getRepository(\App\Entity\User::class)->find((int)$data);
        return new JsonResponse(["committed" => true]);
    }
}
