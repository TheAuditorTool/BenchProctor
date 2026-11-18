// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { Sequelize } from "sequelize";

export const annotateDigest = async (req: Request, res: Response): Promise<void> => {
  const blurb = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const parts: string[] = [];
  for (const token of String(blurb).split(',')) { parts.push(token); }
  const handshake: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const citation = handshake;
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + citation + "'");
  res.json({ accepted: true });
}
