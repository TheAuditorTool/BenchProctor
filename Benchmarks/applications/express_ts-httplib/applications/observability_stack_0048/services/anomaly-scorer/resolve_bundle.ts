// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const resolveBundle = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(excerpt).split(',')) { parts.push(token); }
  const gauge: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(gauge)) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + cohort + "'"));
  res.json({ accepted: true });
}
