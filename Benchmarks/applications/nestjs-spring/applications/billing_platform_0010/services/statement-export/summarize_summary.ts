// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("statement-export")
export class SummarizeSummary {
  @Post("summarizeSummary")
  async summarizeSummary(@Req() req: Request): Promise<unknown> {
    const headline = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const remittance = headline != null ? headline : '';
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle({ client: new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
    await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + remittance + "'"));
    return { created: true };
  }
}
