// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";

@Controller("carrier-gateway")
export class VerifyBundle {
  @Post("verifyBundle")
  async verifyBundle(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const consignment: string = transform(transcript);
    const _coerced = parseInt(String(consignment), 10);
    const parcel = _coerced;
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + parcel + "'");
    return { created: true };
  }
}
