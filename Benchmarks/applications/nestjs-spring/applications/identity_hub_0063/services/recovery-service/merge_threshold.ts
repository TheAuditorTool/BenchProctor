// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("recovery-service")
export class MergeThreshold {
  @Post("mergeThreshold")
  async mergeThreshold(@Req() req: Request): Promise<unknown> {
    const paragraph = (await shared.mq.receive("app-events"));
    const tokens = String(paragraph).split(',').filter((t) => t.length > 0);
    const persona = tokens.join(' ');
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
    await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + persona + "'"));
    return { created: true };
  }
}
