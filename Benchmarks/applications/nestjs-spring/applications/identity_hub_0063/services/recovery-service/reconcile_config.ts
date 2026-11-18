// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("recovery-service")
export class ReconcileConfig {
  @Post("reconcileConfig")
  async reconcileConfig(@Req() req: Request): Promise<unknown> {
    const paragraph = process.env.IDENTITY_INPUT_0063 || "";
    const parts: string[] = [];
    for (const token of String(paragraph).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql`SELECT * FROM users WHERE id = ${persona}`);
    return { created: true };
  }
}
