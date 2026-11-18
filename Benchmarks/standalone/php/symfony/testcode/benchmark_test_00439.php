<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\ORM\EntityManagerInterface;

#[Route('/BenchmarkTest00439', methods: ['POST'])]
class BenchmarkTest00439Controller
{
    public function __invoke(EntityManagerInterface $em)
    {
        $userInput = getenv('APP_VALUE') ?: '';
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $em->getRepository(\App\Entity\User::class)->find((int)$data);
        return new JsonResponse(["committed" => true]);
    }
}
