// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const archiveReceipt = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(remark);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const notice = persona;
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT id, name FROM users WHERE name = '" + notice + "'"));
  res.json({ accepted: true });
}
