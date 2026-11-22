// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import Database from "better-sqlite3";

export const BenchmarkTest00053 = async (req: Request, res: Response): Promise<void> => {
  const userInput = process.env.APP_INPUT || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const appDb = ((globalThis as unknown as { _appDb?: InstanceType<typeof Database> })._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = '" + data + "'").all();
  res.json({ accepted: true });
}
