// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("case-service")
export class LoadIndex {
  @Post("loadIndex")
  async loadIndex(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.authorization as string) || "";
    const tokens = String(synopsis).split(',').filter((t) => t.length > 0);
    const verdict = tokens.join(' ');
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = :id", { replacements: { id: verdict } });
    return { created: true };
  }
}
