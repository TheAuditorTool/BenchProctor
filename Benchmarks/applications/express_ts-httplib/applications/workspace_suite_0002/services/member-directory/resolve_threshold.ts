// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const resolveThreshold = async (req: Request, res: Response): Promise<void> => {
  const transcript = process.env.WORKSPACE_INPUT_0002 || "";
  const _raw = transcript;
  const heading = (_raw && _raw.length > 0) ? _raw : 'default';
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + heading + "'");
  res.json({ accepted: true });
}
