// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { Sequelize } from "sequelize";

export const pruneProfile = async (req: Request, res: Response): Promise<void> => {
  const excerpt = ((req as any).file?.originalname as string) || "";
  const _raw = excerpt;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + persona + "'");
  res.json({ accepted: true });
}
