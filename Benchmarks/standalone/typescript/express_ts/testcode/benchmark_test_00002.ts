// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00002 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await shared.mq.receive("app-events"));
  const data = String(userInput).split(/[ \t]+/).join(" ");
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  res.json({ accepted: true });
}
