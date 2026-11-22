// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { Sequelize } from "sequelize";

@Controller("address-validator")
export class EnrichIndex {
  @Post("enrichIndex")
  async enrichIndex(@Req() req: Request): Promise<unknown> {
    const quotation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const parcel = quotation != null ? quotation : '';
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + parcel + "'");
    return { created: true };
  }
}
