// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("manifest-builder")
export class ArchiveSnapshot {
  @Post("archiveSnapshot")
  async archiveSnapshot(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.authorization as string) || "";
    const tokens = String(footnote).split(',').filter((t) => t.length > 0);
    const consignment = tokens.join(' ');
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = :id", { replacements: { id: consignment } });
    return { created: true };
  }
}
