// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("audit-log")
export class ValidateTenant {
  @Post("validateTenant")
  async validateTenant(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.body as string) || "";
    const persona = Buffer.from(subtitle, "utf-8").toString();
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql`SELECT id, name FROM users WHERE name = ${persona}`);
    return { created: true };
  }
}
