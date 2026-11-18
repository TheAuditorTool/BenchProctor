// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("consent-registry")
export class NormalizeSnapshot {
  @Post("normalizeSnapshot")
  async normalizeSnapshot(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.authorization as string) || "";
    const tokens = String(phrase).split(',').filter((t) => t.length > 0);
    const persona = tokens.join(' ');
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql`SELECT * FROM users WHERE id = ${persona}`);
    return { created: true };
  }
}
