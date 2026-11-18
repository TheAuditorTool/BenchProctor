// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import knex from "knex";

@Controller("member-directory")
export class AuditIndex {
  @Post("auditIndex")
  async auditIndex(@Req() req: Request): Promise<unknown> {
    const transcript = fs.readFileSync("/tmp/data", "utf8");
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const heading: string = parts.join(',');
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + heading + "'");
    return { created: true };
  }
}
