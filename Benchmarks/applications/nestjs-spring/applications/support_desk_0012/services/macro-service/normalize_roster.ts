// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("macro-service")
export class NormalizeRoster {
  @Post("normalizeRoster")
  async normalizeRoster(@Req() req: Request): Promise<unknown> {
    const summary = process.env.SUPPORT_INPUT_0012 || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const grievance: string = parts.join(',');
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql`SELECT * FROM users WHERE id = ${grievance}`);
    return { created: true };
  }
}
