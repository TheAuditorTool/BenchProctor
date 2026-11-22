// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

@Controller("sampling-config")
export class RenderManifest {
  @Post("renderManifest")
  async renderManifest(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const gauge: string = transform(remark);
    const _coerced = parseInt(String(gauge), 10);
    const cohort = _coerced;
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + cohort + "'");
    return { created: true };
  }
}
