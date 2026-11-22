// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("statement-export")
export class ResolveHeader {
  @Post("resolveHeader")
  async resolveHeader(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const remittance: string = transform(headline);
    const _coerced = parseInt(String(remittance), 10);
    const dunning = _coerced;
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle({ client: new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
    await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + dunning + "'"));
    return { created: true };
  }
}
