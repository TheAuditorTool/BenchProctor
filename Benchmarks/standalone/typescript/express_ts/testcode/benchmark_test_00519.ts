// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00519 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ accepted: true });
}
