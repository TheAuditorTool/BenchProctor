// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";

@Controller("message-api")
export class PublishSchedule {
  @Post("publishSchedule")
  async publishSchedule(@Req() req: Request): Promise<unknown> {
    const summary = process.env.MESSAGING_INPUT_0013 || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const bulletin: string = parts.join(',');
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = ?", [bulletin]);
    return { created: true };
  }
}
