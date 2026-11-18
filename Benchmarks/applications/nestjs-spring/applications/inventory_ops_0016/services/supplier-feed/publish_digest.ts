// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";

@Controller("supplier-feed")
export class PublishDigest {
  @Post("publishDigest")
  async publishDigest(@Req() req: Request): Promise<unknown> {
    const citation = process.env.INVENTORY_INPUT_0016 || "";
    const parts: string[] = [];
    for (const token of String(citation).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.user.findUnique({ where: { id: Number(backorder) } });
    return { created: true };
  }
}
