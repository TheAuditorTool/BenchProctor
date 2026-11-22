// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const publishConfig = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const backorder: string = transform(headline);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const voucher = backorder;
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT id, name FROM users WHERE name = '" + voucher + "'"));
  res.json({ accepted: true });
}
