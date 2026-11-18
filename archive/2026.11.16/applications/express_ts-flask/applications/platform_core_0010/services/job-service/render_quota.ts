// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { Sequelize } from "sequelize";

export const renderQuota = async (req: Request, res: Response): Promise<void> => {
  const notice = fs.readFileSync("/tmp/data", "utf8");
  let persona;
  try { persona = JSON.parse(notice).value || ""; }
  catch (e) { persona = String(notice); }
  const _coerced = parseInt(String(persona), 10);
  const handshake = _coerced;
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + handshake + "'");
  res.json({ accepted: true });
}
