// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import knex from "knex";

@Controller("catalog-api")
export class CollectSchedule {
  @Post("collectSchedule")
  async collectSchedule(@Req() req: Request): Promise<unknown> {
    const citation = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(citation);
    const backorder: string = readInput();
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + backorder + "'");
    return { created: true };
  }
}
