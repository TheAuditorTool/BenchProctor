// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import { escapeIdentifier } from "pg";

export const BenchmarkTest00273 = async (req: Request, res: Response): Promise<void> => {
  const userInput = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const data = userInput != null ? userInput : '';
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
  res.json({ accepted: true });
}
