// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("order-api")
export class AnnotatePromotion {
  @Post("annotatePromotion")
  async annotatePromotion(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const backorder: string = transform(headline);
    const _coerced = parseInt(String(backorder), 10);
    const voucher = _coerced;
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + voucher + "'"));
    return { created: true };
  }
}
