// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("audit-log")
export class CompactFlag {
  @Post("compactFlag")
  async compactFlag(@Req() req: Request): Promise<unknown> {
    const passage = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
    let persona;
    try { persona = JSON.parse(passage).value || ""; }
    catch (e) { persona = String(passage); }
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + persona + "'"));
    return { created: true };
  }
}
