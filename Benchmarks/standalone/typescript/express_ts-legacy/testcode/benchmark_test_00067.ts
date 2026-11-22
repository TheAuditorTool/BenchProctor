// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";
import { createClient } from "redis";

export const BenchmarkTest00067 = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.select("id", "name").from("users").orderByRaw(processed);
  res.json({ accepted: true });
}
