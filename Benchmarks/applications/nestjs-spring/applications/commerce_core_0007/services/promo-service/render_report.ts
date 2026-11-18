// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";

@Controller("promo-service")
export class RenderReport {
  @Post("renderReport")
  async renderReport(@Req() req: Request): Promise<unknown> {
    const heading = process.env.ORDERS_INPUT_0007 || "";
    const parts: string[] = [];
    for (const token of String(heading).split(',')) { parts.push(token); }
    const voucher: string = parts.join(',');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.user.findUnique({ where: { id: Number(voucher) } });
    return { created: true };
  }
}
