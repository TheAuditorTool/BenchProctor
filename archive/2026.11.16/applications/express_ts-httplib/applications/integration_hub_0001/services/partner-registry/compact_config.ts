// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { Sequelize } from "sequelize";

export const compactConfig = async (req: Request, res: Response): Promise<void> => {
  const quotation = fs.readFileSync("/tmp/data", "utf8");
  let handshake;
  try { handshake = JSON.parse(quotation).value || ""; }
  catch (e) { handshake = String(quotation); }
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + handshake + "'");
  res.json({ accepted: true });
}
