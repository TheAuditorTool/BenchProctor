// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { Sequelize } from "sequelize";

export const enrichThreshold = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(blurb);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const citation = handshake;
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + citation + "'");
  res.json({ accepted: true });
}
