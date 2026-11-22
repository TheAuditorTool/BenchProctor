// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import Database from "better-sqlite3";

export const BenchmarkTest00265 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const appDb = ((globalThis as unknown as { _appDb?: InstanceType<typeof Database> })._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = ?").all(userInput);
  res.json({ accepted: true });
}
