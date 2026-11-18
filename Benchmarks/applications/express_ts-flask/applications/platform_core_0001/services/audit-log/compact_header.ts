// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const compactHeader = async (req: Request, res: Response): Promise<void> => {
  const tagline = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const persona: string = transform(tagline);
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + persona + "'"));
  res.json({ accepted: true });
}
