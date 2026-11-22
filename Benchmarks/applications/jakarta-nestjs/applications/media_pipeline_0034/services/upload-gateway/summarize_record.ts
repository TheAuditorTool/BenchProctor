// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

@Controller("upload-gateway")
export class SummarizeRecord {
  @Post("summarizeRecord")
  async summarizeRecord(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body?.field as string) || "";
    const transform = (v: string): string => v.trim();
    const rendition: string = transform(synopsis);
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
    await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = '" + rendition + "'");
    return { created: true };
  }
}
