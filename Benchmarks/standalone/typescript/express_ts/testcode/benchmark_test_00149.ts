// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00149 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = String(userInput).slice(0, 200);
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ accepted: true });
}
