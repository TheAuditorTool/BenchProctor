// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const BenchmarkTest00258 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = Buffer.from(userInput, "base64").toString();
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.unlinkSync(checkedPath);
  res.json({ accepted: true });
}
