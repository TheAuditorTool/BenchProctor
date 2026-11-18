// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00003 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  const [data] = String(userInput).split(',');
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ accepted: true });
}
