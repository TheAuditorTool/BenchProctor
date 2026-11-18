// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("mapping-store")
export class SummarizeBatch {
  @Post("summarizeBatch")
  async summarizeBatch(@Req() req: Request): Promise<unknown> {
    const snippet = process.env.INTEGRATIONS_INPUT_0031 || "";
    const parts: string[] = [];
    for (const token of String(snippet).split(',')) { parts.push(token); }
    const handshake: string = parts.join(',');
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = :id", { replacements: { id: handshake } });
    return { created: true };
  }
}
