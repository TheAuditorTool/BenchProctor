// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";

@Controller("carrier-gateway")
export class AuditShipment {
  @Post("auditShipment")
  async auditShipment(@Req() req: Request): Promise<unknown> {
    const quotation = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const parts: string[] = [];
    for (const token of String(quotation).split(',')) { parts.push(token); }
    const parcel: string = parts.join(',');
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + parcel + "'");
    return { created: true };
  }
}
