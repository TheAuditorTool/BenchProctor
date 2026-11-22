// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00011 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const data = decodeURIComponent(userInput);
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ accepted: true });
}
