// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import Database from "better-sqlite3";

export const BenchmarkTest00036 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await shared.mq.receive("app-events"));
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  const appDb = ((globalThis as unknown as { _appDb?: InstanceType<typeof Database> })._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  const orderColumn = '"' + String(data).replace(/"/g, '""') + '"';
  appDb.prepare("SELECT id, name FROM users ORDER BY " + orderColumn).all();
  res.json({ accepted: true });
}
