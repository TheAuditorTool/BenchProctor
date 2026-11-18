// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const BenchmarkTest00476 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = `${userInput}`;
  const checkedPath = "/var/app/data/" + path.basename(data);
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  res.send(fileContent);
}
