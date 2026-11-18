// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const BenchmarkTest00153 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.writeFileSync(checkedPath, "data");
  res.json({ accepted: true });
}
