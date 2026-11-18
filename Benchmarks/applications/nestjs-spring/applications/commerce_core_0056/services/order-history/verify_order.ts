// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";

@Controller("order-history")
export class VerifyOrder {
  @Post("verifyOrder")
  async verifyOrder(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.authorization as string) || "";
    const tokens = String(citation).split(',').filter((t) => t.length > 0);
    const backorder = tokens.join(' ');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.user.findUnique({ where: { id: Number(backorder) } });
    return { created: true };
  }
}
