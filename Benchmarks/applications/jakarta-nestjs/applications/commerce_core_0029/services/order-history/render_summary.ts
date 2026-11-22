// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

@Controller("order-history")
export class RenderSummary {
  @Post("renderSummary")
  async renderSummary(@Req() req: Request): Promise<unknown> {
    const notice = fs.readFileSync("/tmp/data", "utf8");
    const backorder = notice != null ? notice : '';
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
    await _prisma.user.findUnique({ where: { id: Number(backorder) } });
    return { created: true };
  }
}
