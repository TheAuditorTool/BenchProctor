// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const annotatePromotion = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body.payload as string) || "";
  let backorder;
  try { backorder = JSON.parse(headline).value || ""; }
  catch (e) { backorder = String(headline); }
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql`SELECT id, name FROM users WHERE name = ${backorder}`);
  res.json({ accepted: true });
}
