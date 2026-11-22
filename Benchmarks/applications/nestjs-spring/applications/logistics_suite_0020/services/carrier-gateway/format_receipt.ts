// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import knex from "knex";

@Controller("carrier-gateway")
export class FormatReceipt {
  @Post("formatReceipt")
  async formatReceipt(@Req() req: Request): Promise<unknown> {
    const transcript = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const consignment = transcript != null ? transcript : '';
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + consignment + "'");
    return { created: true };
  }
}
