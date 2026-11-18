// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import knex from "knex";

@Controller("message-api")
export class NormalizeSnapshot {
  @Post("normalizeSnapshot")
  async normalizeSnapshot(@Req() req: Request): Promise<unknown> {
    const summary = (await shared.mq.receive("app-events"));
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const bulletin = tokens.join(' ');
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + bulletin + "'");
    return { created: true };
  }
}
