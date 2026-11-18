// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { escapeIdentifier } from "pg";

export const BenchmarkTest00067 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
  res.json({ accepted: true });
}
