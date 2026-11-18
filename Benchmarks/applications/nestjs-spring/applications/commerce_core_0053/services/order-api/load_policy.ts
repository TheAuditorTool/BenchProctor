// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("order-api")
export class LoadPolicy {
  @Post("loadPolicy")
  async loadPolicy(@Req() req: Request): Promise<unknown> {
    const memo = fs.readFileSync("/tmp/data", "utf8");
    const parts: string[] = [];
    for (const token of String(memo).split(',')) { parts.push(token); }
    const voucher: string = parts.join(',');
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + voucher + "'"));
    return { created: true };
  }
}
