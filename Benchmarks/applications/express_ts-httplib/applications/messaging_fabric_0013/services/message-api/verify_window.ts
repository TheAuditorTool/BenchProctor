// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const verifyWindow = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const bulletin: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const snippet = bulletin;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + snippet + "'");
  res.json({ accepted: true });
}
