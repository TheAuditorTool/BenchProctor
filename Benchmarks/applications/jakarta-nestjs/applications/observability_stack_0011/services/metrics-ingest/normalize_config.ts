// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";

@Controller("metrics-ingest")
export class NormalizeConfig {
  @Post("normalizeConfig")
  async normalizeConfig(@Req() req: Request): Promise<unknown> {
    const caption = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const gauge = caption != null ? caption : '';
    const _coerced = parseInt(String(gauge), 10);
    const cohort = _coerced;
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + cohort + "'");
    return { created: true };
  }
}
