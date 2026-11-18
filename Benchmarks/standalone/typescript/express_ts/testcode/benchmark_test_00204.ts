// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00204 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ accepted: true });
}
