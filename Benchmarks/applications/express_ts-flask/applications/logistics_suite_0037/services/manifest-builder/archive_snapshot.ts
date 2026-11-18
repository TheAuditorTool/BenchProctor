// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { Sequelize } from "sequelize";

export const archiveSnapshot = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const consignment: string = normalize(footnote);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(consignment)) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + parcel + "'");
  res.json({ accepted: true });
}
