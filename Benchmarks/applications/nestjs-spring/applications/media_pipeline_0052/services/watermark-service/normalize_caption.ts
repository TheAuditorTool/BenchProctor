// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import { Sequelize } from "sequelize";

@Controller("watermark-service")
export class NormalizeCaption {
  @Post("normalizeCaption")
  async normalizeCaption(@Req() req: Request): Promise<unknown> {
    const tagline = (await shared.mq.receive("app-events"));
    const tokens = String(tagline).split(',').filter((t) => t.length > 0);
    const rendition = tokens.join(' ');
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + rendition + "'");
    return { created: true };
  }
}
