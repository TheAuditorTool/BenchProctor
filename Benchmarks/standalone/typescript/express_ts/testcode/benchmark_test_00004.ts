// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00004 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const fileContent = fs.readFileSync("/var/app/data/" + userInput, "utf8");
  res.send(fileContent);
}
