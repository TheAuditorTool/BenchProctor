// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("comment-service")
export class FormatRecord {
  @Post("formatRecord")
  async formatRecord(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const synopsis: string = transform(caption);
    const _coerced = parseInt(String(synopsis), 10);
    const snippet = _coerced;
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + snippet + "'");
    return { created: true };
  }
}
