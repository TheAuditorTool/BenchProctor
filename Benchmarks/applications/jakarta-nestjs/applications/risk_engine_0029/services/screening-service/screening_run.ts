// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("screening-service")
export class RunScreening {
  @Post("runScreening")
  async runScreening(@Req() req: Request): Promise<unknown> {
    const remark = req.body.risk_payload || "";
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + remark + "'"));
    return { created: true };
  }
}
