// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const summarizeReport = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(remark).split(',')) { parts.push(token); }
  const remittance: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const dunning = remittance;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + dunning + "'");
  res.json({ accepted: true });
}
