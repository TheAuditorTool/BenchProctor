// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00183 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.host as string) || "";
  const data = `${userInput}`;
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}
