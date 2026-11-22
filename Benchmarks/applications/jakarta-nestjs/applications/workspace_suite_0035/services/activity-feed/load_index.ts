// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("activity-feed")
export class LoadIndex {
  @Post("loadIndex")
  async loadIndex(@Req() req: Request): Promise<unknown> {
    const paragraph = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const parts: string[] = [];
    for (const token of String(paragraph).split(',')) { parts.push(token); }
    const wording: string = parts.join(',');
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + wording + "'"));
    return { created: true };
  }
}
