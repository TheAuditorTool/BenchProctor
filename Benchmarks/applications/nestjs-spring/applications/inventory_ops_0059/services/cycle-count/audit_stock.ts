// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";
import { createClient } from "redis";

@Controller("cycle-count")
export class AuditStock {
  @Post("auditStock")
  async auditStock(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const memo = (await _cache.get("user_data")) || "";
    const backorder = Buffer.from(memo, "base64").toString();
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + backorder + "'");
    return { created: true };
  }
}
