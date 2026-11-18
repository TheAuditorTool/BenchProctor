// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const compactLedger = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(passage).split(',')) { parts.push(token); }
  const dossier: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(dossier)) { res.status(400).json({error:"invalid"}); return; }
  const addendum = dossier;
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + addendum + "'"));
  res.json({ accepted: true });
}
