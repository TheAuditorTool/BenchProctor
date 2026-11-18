// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const enrichManifest = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.query.id as string) || "";
  const _raw = snippet;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + persona + "'");
  res.json({ accepted: true });
}
