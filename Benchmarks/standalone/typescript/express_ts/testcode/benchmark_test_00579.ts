// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00579 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}
