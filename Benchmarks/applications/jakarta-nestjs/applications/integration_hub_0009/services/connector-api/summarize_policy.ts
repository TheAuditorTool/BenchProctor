// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import { DataTypes, Sequelize } from "sequelize";

@Controller("connector-api")
export class SummarizePolicy {
  @Post("summarizePolicy")
  async summarizePolicy(@Req() req: Request): Promise<unknown> {
    const heading = (await shared.mq.receive("app-events"));
    const handshake = Buffer.from(heading, "base64").toString();
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
    await User.findAll({ where: _sequelize.literal("name = '" + handshake + "'") });
    return { created: true };
  }
}
