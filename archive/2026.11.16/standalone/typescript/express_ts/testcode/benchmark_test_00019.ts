// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";
import * as nodeUtil from "util";

export const BenchmarkTest00019 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  const data = nodeUtil.format("%s", userInput);
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.unlinkSync(checkedPath);
  res.json({ accepted: true });
}
