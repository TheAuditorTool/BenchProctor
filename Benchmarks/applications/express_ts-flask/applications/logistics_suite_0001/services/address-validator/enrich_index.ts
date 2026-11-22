// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataTypes, Sequelize } from "sequelize";

export const enrichIndex = async (req: Request, res: Response): Promise<void> => {
  const quotation = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const parcel = quotation != null ? quotation : '';
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = '" + parcel + "'") });
  res.json({ accepted: true });
}
