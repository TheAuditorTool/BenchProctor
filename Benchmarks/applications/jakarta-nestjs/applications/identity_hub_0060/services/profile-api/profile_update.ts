// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

@Controller("profile-api")
export class UpdateProfile {
  @Post("updateProfile")
  async updateProfile(@Req() req: Request): Promise<unknown> {
    const phrase = req.body.identity_payload || "";
    const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle({ client: new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
    await _drizzle.execute(sql.raw("SELECT id, name FROM users WHERE name = '" + phrase + "'"));
    return { created: true };
  }
}
