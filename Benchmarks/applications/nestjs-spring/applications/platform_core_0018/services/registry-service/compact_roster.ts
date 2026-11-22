// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("registry-service")
export class CompactRoster {
  @Post("compactRoster")
  async compactRoster(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const persona: string = transform(subtitle);
    const _coerced = parseInt(String(persona), 10);
    const handshake = _coerced;
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + handshake + "'");
    return { created: true };
  }
}
