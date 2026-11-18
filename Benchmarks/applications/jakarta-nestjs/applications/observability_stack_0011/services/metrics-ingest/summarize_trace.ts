// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import knex from "knex";

@Controller("metrics-ingest")
export class SummarizeTrace {
  @Post("summarizeTrace")
  async summarizeTrace(@Req() req: Request): Promise<unknown> {
    const caption = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
    let gauge;
    try { gauge = JSON.parse(caption).value || ""; }
    catch (e) { gauge = String(caption); }
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + gauge + "'");
    return { created: true };
  }
}
