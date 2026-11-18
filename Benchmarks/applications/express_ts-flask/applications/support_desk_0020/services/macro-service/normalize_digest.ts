// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const normalizeDigest = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.query.id as string) || "";
  const _raw = phrase;
  const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + inquiry + "'"));
  res.json({ accepted: true });
}
