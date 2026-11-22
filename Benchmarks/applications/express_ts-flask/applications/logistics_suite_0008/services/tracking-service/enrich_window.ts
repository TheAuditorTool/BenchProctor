// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { Sequelize } from "sequelize";

export const enrichWindow = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.query.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(caption);
  const consignment: string = readInput();
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + consignment + "'");
  res.json({ accepted: true });
}
