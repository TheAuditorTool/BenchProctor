// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("manifest-builder")
export class BuildBatch {
  @Post("buildBatch")
  async buildBatch(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const consignment: string = transform(wording);
    const _coerced = parseInt(String(consignment), 10);
    const parcel = _coerced;
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + parcel + "'");
    return { created: true };
  }
}
