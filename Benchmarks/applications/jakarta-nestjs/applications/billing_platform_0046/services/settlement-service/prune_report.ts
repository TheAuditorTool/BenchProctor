// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";

@Controller("settlement-service")
export class PruneReport {
  @Post("pruneReport")
  async pruneReport(@Req() req: Request): Promise<unknown> {
    const remark = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const remittance = remark != null ? remark : '';
    const _coerced = parseInt(String(remittance), 10);
    const arrears = _coerced;
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + arrears + "'");
    return { created: true };
  }
}
