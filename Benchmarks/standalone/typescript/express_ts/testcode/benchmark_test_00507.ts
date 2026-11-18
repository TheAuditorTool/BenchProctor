// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { escapeIdentifier } from "pg";

export const BenchmarkTest00507 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(userInput)));
  res.json({ accepted: true });
}
