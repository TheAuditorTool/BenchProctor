// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { Sequelize } from "sequelize";

export const exportDigest = async (req: Request, res: Response): Promise<void> => {
  const blurb = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const tokens = String(blurb).split(',').filter((t) => t.length > 0);
  const handshake = tokens.join(' ');
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + handshake + "'");
  res.json({ accepted: true });
}
