// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("anomaly-scorer")
export class ResolveReport {
  @Post("resolveReport")
  async resolveReport(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.authorization as string) || "";
    const tokens = String(excerpt).split(',').filter((t) => t.length > 0);
    const gauge = tokens.join(' ');
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql`SELECT * FROM users WHERE id = ${gauge}`);
    return { created: true };
  }
}
