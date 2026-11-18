// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { drizzle } from "drizzle-orm/node-postgres";
import { sql } from "drizzle-orm";
import { Pool } from "pg";

export const auditSchedule = async (req: Request, res: Response): Promise<void> => {
  const preface = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const bulletin = Buffer.from(preface, "base64").toString();
  const _coerced = parseInt(String(bulletin), 10);
  const notice = _coerced;
  const _drizzle = ((globalThis as unknown as { _drizzle?: ReturnType<typeof drizzle> })._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + notice + "'"));
  res.json({ accepted: true });
}
