// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import { Sequelize } from "sequelize";

export const formatDigest = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const verdict: string = transform(excerpt);
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + verdict + "'");
  res.json({ accepted: true });
}
