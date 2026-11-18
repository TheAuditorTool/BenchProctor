// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import knex from "knex";

@Controller("payout-service")
export class CollectReport {
  @Post("collectReport")
  async collectReport(@Req() req: Request): Promise<unknown> {
    const headline = (await shared.mq.receive("app-events"));
    const tokens = String(headline).split(',').filter((t) => t.length > 0);
    const disbursement = tokens.join(' ');
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + disbursement + "'");
    return { created: true };
  }
}
