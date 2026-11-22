// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";

@Controller("member-directory")
export class NormalizeRoster {
  @Post("normalizeRoster")
  async normalizeRoster(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body as string) || "";
    const wording = Buffer.from(paragraph, "base64").toString();
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.select("id", "name").from("users").whereRaw("name = '" + wording + "'");
    return { created: true };
  }
}
