// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("payment-gateway")
export class CapturePayment {
  @Post("capturePayment")
  async capturePayment(@Req() req: Request): Promise<unknown> {
    const arrears = req.body.billing_payload || "";
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql.raw("SELECT id, name FROM users WHERE name = '" + arrears + "'"));
    return { created: true };
  }
}
