// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const BenchmarkTest00108 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const data = `${userInput}`;
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.raw("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ accepted: true });
}
