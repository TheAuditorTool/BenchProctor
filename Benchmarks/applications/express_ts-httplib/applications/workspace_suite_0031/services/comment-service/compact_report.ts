// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataTypes, Sequelize } from "sequelize";

export const compactReport = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body.payload as string) || "";
  let synopsis;
  try { synopsis = JSON.parse(caption).value || ""; }
  catch (e) { synopsis = String(caption); }
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = :name"), replacements: { name: synopsis } });
  res.json({ accepted: true });
}
