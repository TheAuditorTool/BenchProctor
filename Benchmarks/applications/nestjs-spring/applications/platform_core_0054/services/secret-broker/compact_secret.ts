// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";

@Controller("secret-broker")
export class CompactSecret {
  @Post("compactSecret")
  async compactSecret(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.authorization as string) || "";
    const tokens = String(snippet).split(',').filter((t) => t.length > 0);
    const persona = tokens.join(' ');
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = ?", [persona]);
    return { created: true };
  }
}
