// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { Sequelize } from "sequelize";

export const annotateSchedule = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(note);
  const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = :id", { replacements: { id: handshake } });
  res.json({ accepted: true });
}
