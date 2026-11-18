// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00591 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = String(userInput).replace(/\u0000/g, "");
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(String(parsedNum));
  res.json({ accepted: true });
}
