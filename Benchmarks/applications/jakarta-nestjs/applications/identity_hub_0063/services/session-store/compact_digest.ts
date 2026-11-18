// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";
import { createClient } from "redis";

@Controller("session-store")
export class CompactDigest {
  @Post("compactDigest")
  async compactDigest(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const paragraph = (await _cache.get("user_data")) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(paragraph);
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + persona + "'");
    return { created: true };
  }
}
