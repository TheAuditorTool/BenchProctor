// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";

@Controller("share-service")
export class PruneSchedule {
  @Post("pruneSchedule")
  async pruneSchedule(@Req() req: Request): Promise<unknown> {
    const preface = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const remark = preface != null ? preface : '';
    const _coerced = parseInt(String(remark), 10);
    const wording = _coerced;
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + wording + "'");
    return { created: true };
  }
}
