// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";
import { createClient } from "redis";

@Controller("capture-service")
export class CollectHeader {
  @Post("collectHeader")
  async collectHeader(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const caption = (await _cache.get("user_data")) || "";
    const tokens = String(caption).split(',').filter((t) => t.length > 0);
    const ledger = tokens.join(' ');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + ledger + "'");
    return { created: true };
  }
}
