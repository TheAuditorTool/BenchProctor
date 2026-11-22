// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00316 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const data = `${userInput}`;
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ accepted: true });
}
