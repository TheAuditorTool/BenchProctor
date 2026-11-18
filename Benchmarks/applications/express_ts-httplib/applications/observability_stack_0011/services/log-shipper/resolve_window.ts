// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { Sequelize } from "sequelize";
import { createClient } from "redis";

export const resolveWindow = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const caption = (await _cache.get("user_data")) || "";
  const _raw = caption;
  const gauge = (_raw && _raw.length > 0) ? _raw : 'default';
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + gauge + "'");
  res.json({ accepted: true });
}
