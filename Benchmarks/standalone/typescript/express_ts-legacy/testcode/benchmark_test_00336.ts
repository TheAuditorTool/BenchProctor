// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00336 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ accepted: true });
}
