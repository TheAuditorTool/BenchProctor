// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { drizzle } from "drizzle-orm/better-sqlite3";
import { sql } from "drizzle-orm";
import Database from "better-sqlite3";

export const BenchmarkTest00356 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.run(sql.raw("SELECT * FROM users WHERE id = '" + data + "'"));
  res.json({ accepted: true });
}
