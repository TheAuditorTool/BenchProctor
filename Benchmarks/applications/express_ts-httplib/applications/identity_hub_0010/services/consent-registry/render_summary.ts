// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const renderSummary = async (req: Request, res: Response): Promise<void> => {
  const phrase = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const parts: string[] = [];
  for (const token of String(phrase).split(',')) { parts.push(token); }
  const persona: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const transcript = persona;
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + transcript + "'"));
  res.json({ accepted: true });
}
