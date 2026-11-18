// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const normalizeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const disbursement: string = normalize(headline);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(disbursement)) { res.status(400).json({error:"invalid"}); return; }
  const remittance = disbursement;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + remittance + "'");
  res.json({ accepted: true });
}
