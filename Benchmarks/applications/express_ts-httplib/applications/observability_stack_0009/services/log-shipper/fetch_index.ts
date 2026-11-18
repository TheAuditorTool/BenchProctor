// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { Sequelize } from "sequelize";

export const fetchIndex = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const gauge: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(gauge)) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + cohort + "'");
  res.json({ accepted: true });
}
