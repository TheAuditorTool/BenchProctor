// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";
import { createClient } from "redis";

@Controller("partner-registry")
export class ExportDigest {
  @Post("exportDigest")
  async exportDigest(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const blurb = (await _cache.get("user_data")) || "";
    const tokens = String(blurb).split(',').filter((t) => t.length > 0);
    const handshake = tokens.join(' ');
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + handshake + "'");
    return { created: true };
  }
}
