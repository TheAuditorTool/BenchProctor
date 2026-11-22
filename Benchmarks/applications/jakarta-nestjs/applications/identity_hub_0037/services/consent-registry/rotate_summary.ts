// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("consent-registry")
export class RotateSummary {
  @Post("rotateSummary")
  async rotateSummary(@Req() req: Request): Promise<unknown> {
    const remark = (req.body as string) || "";
    const persona = Buffer.from(remark, "utf-8").toString();
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql`SELECT id, name FROM users WHERE name = ${persona}`);
    return { created: true };
  }
}
