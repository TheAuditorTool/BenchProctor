// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { Sequelize } from "sequelize";

export const archiveConfig = async (req: Request, res: Response): Promise<void> => {
  const tagline = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const rendition = Buffer.from(tagline, "base64").toString();
  const _coerced = parseInt(String(rendition), 10);
  const montage = _coerced;
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + montage + "'");
  res.json({ accepted: true });
}
