// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";
import { createClient } from "redis";

@Controller("sampling-config")
export class CollectSnapshot {
  @Post("collectSnapshot")
  async collectSnapshot(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const preface = (await _cache.get("user_data")) || "";
    const cohort = preface != null ? preface : '';
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + cohort + "'");
    return { created: true };
  }
}
