// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00665 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}
