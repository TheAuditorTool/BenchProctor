// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as nodeUtil from "util";
import Database from "better-sqlite3";

export const BenchmarkTest00273 = async (req: Request, res: Response): Promise<void> => {
  const userInput = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const data = nodeUtil.format("%s", userInput);
  const appDb = ((globalThis as unknown as { _appDb?: InstanceType<typeof Database> })._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = ?").all(data);
  res.json({ accepted: true });
}
