// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("presence-service")
export class MergeLedger {
  @Post("mergeLedger")
  async mergeLedger(@Req() req: Request): Promise<unknown> {
    const footnote = fs.readFileSync("/tmp/data", "utf8");
    const bulletin = footnote != null ? footnote : '';
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle({ client: new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
    await _drizzle.execute(sql`SELECT * FROM users WHERE id = ${bulletin}`);
    return { created: true };
  }
}
