// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataTypes, Sequelize } from "sequelize";

@Controller("dunning-service")
export class BuildInvoice {
  @Post("buildInvoice")
  async buildInvoice(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body?.field as string) || "";
    const transform = (v: string): string => v.trim();
    const remittance: string = transform(footnote);
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
    await User.findAll({ where: _sequelize.literal("name = '" + remittance + "'") });
    return { created: true };
  }
}
