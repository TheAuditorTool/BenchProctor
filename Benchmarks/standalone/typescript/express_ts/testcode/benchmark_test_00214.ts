// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { escapeIdentifier } from "pg";

export const BenchmarkTest00214 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
  res.json({ accepted: true });
}
