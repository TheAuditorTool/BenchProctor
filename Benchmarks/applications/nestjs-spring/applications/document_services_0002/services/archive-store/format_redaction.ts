// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("archive-store")
export class FormatRedaction {
  @Post("formatRedaction")
  async formatRedaction(@Req() req: Request): Promise<unknown> {
    const wording = (req.body as string) || "";
    const addendum = Buffer.from(wording, "base64").toString();
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql.raw("SELECT id, name FROM users WHERE name = '" + addendum + "'"));
    return { created: true };
  }
}
