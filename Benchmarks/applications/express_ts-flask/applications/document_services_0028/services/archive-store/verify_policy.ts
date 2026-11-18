// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const verifyPolicy = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const addendum: string = normalize(note);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(addendum)) { res.status(400).json({error:"invalid"}); return; }
  const dossier = addendum;
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + dossier + "'"));
  res.json({ accepted: true });
}
