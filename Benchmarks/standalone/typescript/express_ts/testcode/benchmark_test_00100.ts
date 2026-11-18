// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00100 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.host as string) || "";
  const data = userInput != null ? userInput : '';
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ accepted: true });
}
