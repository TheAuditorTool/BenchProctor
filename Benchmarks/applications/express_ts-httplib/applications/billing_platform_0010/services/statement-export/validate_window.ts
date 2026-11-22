// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const validateWindow = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body.payload as string) || "";
  let remittance;
  try { remittance = JSON.parse(headline).value || ""; }
  catch (e) { remittance = String(headline); }
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql`SELECT id, name FROM users WHERE name = ${remittance}`);
  res.json({ accepted: true });
}
