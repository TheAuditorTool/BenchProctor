// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const annotateProfile = async (req: Request, res: Response): Promise<void> => {
  const paragraph = process.env.MESSAGING_INPUT_0004 || "";
  const _raw = paragraph;
  const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + bulletin + "'");
  res.json({ accepted: true });
}
