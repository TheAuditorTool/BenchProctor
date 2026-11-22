// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import knex from "knex";

export const BenchmarkTest00194 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = nodeUtil.format("%s", userInput);
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.select("id", "name").from("users").whereRaw("name = '" + data + "'");
  res.json({ accepted: true });
}
