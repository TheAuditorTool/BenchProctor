// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("asset-library")
export class SummarizeSummary {
  @Post("summarizeSummary")
  async summarizeSummary(@Req() req: Request): Promise<unknown> {
    const note = (req.headers.referer as string) || "";
    const byline = note != null ? note : '';
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + byline + "'");
    return { created: true };
  }
}
