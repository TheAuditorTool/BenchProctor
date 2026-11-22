// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00177 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await shared.mq.receive("app-events"));
  const data = String(userInput).replace(/\u0000/g, "");
  await db.query("SELECT * FROM users WHERE id = $1", [data]);
  res.json({ accepted: true });
}
