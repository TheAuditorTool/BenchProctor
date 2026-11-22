// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { Sequelize } from "sequelize";

@Controller("connector-api")
export class PruneWebhook {
  @Post("pruneWebhook")
  async pruneWebhook(@Req() req: Request): Promise<unknown> {
    const heading = fs.readFileSync("/tmp/data", "utf8");
    const handshake = heading != null ? heading : '';
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = :id", { replacements: { id: handshake } });
    return { created: true };
  }
}
