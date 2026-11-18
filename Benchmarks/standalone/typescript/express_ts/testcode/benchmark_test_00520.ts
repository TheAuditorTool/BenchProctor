// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00520 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const data = `${userInput}`;
  await db.query("SELECT * FROM users WHERE id = $1", [data]);
  res.json({ accepted: true });
}
