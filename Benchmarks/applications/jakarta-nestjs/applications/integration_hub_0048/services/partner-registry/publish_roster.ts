// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataTypes, Sequelize } from "sequelize";

@Controller("partner-registry")
export class PublishRoster {
  @Post("publishRoster")
  async publishRoster(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    const handshake = Buffer.from(citation, "utf-8").toString();
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
    await User.findAll({ where: _sequelize.literal("name = :name"), replacements: { name: handshake } });
    return { created: true };
  }
}
