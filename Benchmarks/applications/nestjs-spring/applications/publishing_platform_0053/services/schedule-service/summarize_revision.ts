// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("schedule-service")
export class SummarizeRevision {
  @Post("summarizeRevision")
  async summarizeRevision(@Req() req: Request): Promise<unknown> {
    const note = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const byline: string = transform(note);
    const _coerced = parseInt(String(byline), 10);
    const addendum = _coerced;
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + addendum + "'"));
    return { created: true };
  }
}
