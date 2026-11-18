// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { escapeIdentifier } from "pg";

export const BenchmarkTest00444 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
  res.json({ accepted: true });
}
