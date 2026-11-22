// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { drizzle } from "drizzle-orm/better-sqlite3";
import { sql } from "drizzle-orm";
import Database from "better-sqlite3";

export const BenchmarkTest00008 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = Buffer.from(userInput, "base64").toString();
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.all(sql.raw("SELECT id, name FROM users WHERE name = '" + parsedId + "'"));
  res.json({ accepted: true });
}
