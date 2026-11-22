// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";

@Controller("cart-service")
export class RotateProfile {
  @Post("rotateProfile")
  async rotateProfile(@Req() req: Request): Promise<unknown> {
    const headline = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const parts: string[] = [];
    for (const token of String(headline).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + backorder + "'");
    return { created: true };
  }
}
