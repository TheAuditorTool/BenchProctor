// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { DataTypes, Sequelize } from "sequelize";

export const collectWindow = async (req: Request, res: Response): Promise<void> => {
  const heading = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  function normalize(value: string): string { return value.normalize("NFC"); }
  const addendum: string = normalize(heading);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(addendum)) { res.status(400).json({error:"invalid"}); return; }
  const byline = addendum;
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = '" + byline + "'") });
  res.json({ accepted: true });
}
