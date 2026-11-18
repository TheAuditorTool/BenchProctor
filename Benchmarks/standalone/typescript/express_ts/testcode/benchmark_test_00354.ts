// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const BenchmarkTest00354 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const [data] = String(userInput).split(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.raw("SELECT * FROM users WHERE id = '" + processed + "'");
  res.json({ accepted: true });
}
