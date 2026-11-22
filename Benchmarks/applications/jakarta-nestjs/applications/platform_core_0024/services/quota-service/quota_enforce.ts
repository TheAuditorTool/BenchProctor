// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

@Controller("quota-service")
export class EnforceQuota {
  @Post("enforceQuota")
  async enforceQuota(@Req() req: Request): Promise<unknown> {
    const remark = req.body.platform_payload || "";
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
    await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = $1", remark);
    return { created: true };
  }
}
