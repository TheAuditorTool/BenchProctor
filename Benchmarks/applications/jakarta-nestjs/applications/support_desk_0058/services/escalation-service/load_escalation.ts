// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { Sequelize } from "sequelize";

@Controller("escalation-service")
export class LoadEscalation {
  @Post("loadEscalation")
  async loadEscalation(@Req() req: Request): Promise<unknown> {
    const snippet = fs.readFileSync("/tmp/data", "utf8");
    const inquiry = snippet != null ? snippet : '';
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = :id", { replacements: { id: inquiry } });
    return { created: true };
  }
}
