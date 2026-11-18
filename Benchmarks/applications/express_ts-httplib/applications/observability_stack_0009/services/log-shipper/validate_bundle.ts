// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { Sequelize } from "sequelize";

export const validateBundle = async (req: Request, res: Response): Promise<void> => {
  const summary = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const gauge: string = readInput();
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + gauge + "'");
  res.json({ accepted: true });
}
