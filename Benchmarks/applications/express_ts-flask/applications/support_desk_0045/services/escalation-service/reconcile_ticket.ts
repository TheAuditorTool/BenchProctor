// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataTypes, Sequelize } from "sequelize";

export const reconcileTicket = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(remark);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(inquiry)) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = '" + grievance + "'") });
  res.json({ accepted: true });
}
