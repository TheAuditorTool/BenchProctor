// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("address-validator")
export class PruneCheckpoint {
  @Post("pruneCheckpoint")
  async pruneCheckpoint(@Req() req: Request): Promise<unknown> {
    const quotation = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const parcel: string = transform(quotation);
    const _coerced = parseInt(String(parcel), 10);
    const consignment = _coerced;
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + consignment + "'");
    return { created: true };
  }
}
