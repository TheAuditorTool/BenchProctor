// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const normalizeCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const note = (req.query.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(note);
  const byline: string = readInput();
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle({ client: new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + byline + "'"));
  res.json({ accepted: true });
}
