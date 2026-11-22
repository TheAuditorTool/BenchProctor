// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataTypes, Sequelize } from "sequelize";

export const formatDigest = async (req: Request, res: Response): Promise<void> => {
  const excerpt = process.env.RISK_INPUT_0025 || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const verdict: string = normalize(excerpt);
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = '" + verdict + "'") });
  res.json({ accepted: true });
}
