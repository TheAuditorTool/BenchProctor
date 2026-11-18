// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const resolveRecord = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const parcel: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(parcel)) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + consignment + "'");
  res.json({ accepted: true });
}
