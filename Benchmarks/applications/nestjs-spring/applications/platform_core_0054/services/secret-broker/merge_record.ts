// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";

@Controller("secret-broker")
export class MergeRecord {
  @Post("mergeRecord")
  async mergeRecord(@Req() req: Request): Promise<unknown> {
    const snippet = process.env.PLATFORM_INPUT_0054 || "";
    const parts: string[] = [];
    for (const token of String(snippet).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = ?", [persona]);
    return { created: true };
  }
}
