// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import { Sequelize } from "sequelize";

export const validateWindow = async (req: Request, res: Response): Promise<void> => {
  const heading = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(heading);
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + addendum + "'");
  res.json({ accepted: true });
}
