// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const BenchmarkTest00116 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.raw("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ accepted: true });
}
