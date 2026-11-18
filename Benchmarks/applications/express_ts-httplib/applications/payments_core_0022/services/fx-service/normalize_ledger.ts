// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { Sequelize } from "sequelize";

export const normalizeLedger = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(subject).split(',')) { parts.push(token); }
  const ledger: string = parts.join(',');
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + ledger + "'");
  res.json({ accepted: true });
}
