// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { Sequelize } from "sequelize";

export const annotateSchedule = async (req: Request, res: Response): Promise<void> => {
  const note = fs.readFileSync("/tmp/data", "utf8");
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(note);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const persona = handshake;
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + persona + "'");
  res.json({ accepted: true });
}
