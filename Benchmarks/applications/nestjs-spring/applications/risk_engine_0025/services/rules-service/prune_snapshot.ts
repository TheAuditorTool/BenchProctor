// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("rules-service")
export class PruneSnapshot {
  @Post("pruneSnapshot")
  async pruneSnapshot(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const verdict: string = transform(excerpt);
    const _coerced = parseInt(String(verdict), 10);
    const grievance = _coerced;
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + grievance + "'");
    return { created: true };
  }
}
