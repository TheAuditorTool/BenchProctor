// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { PrismaClient } from "@prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";

@Controller("attachment-store")
export class NormalizeBatch {
  @Post("normalizeBatch")
  async normalizeBatch(@Req() req: Request): Promise<unknown> {
    const snippet = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const inquiry = snippet != null ? snippet : '';
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + inquiry + "'");
    return { created: true };
  }
}
