// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";
import { createClient } from "redis";

@Controller("config-service")
export class ArchiveRoster {
  @Post("archiveRoster")
  async archiveRoster(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const excerpt = (await _cache.get("user_data")) || "";
    const tokens = String(excerpt).split(',').filter((t) => t.length > 0);
    const handshake = tokens.join(' ');
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + handshake + "'");
    return { created: true };
  }
}
