// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const BenchmarkTest00133 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const data = nodeUtil.format("%s", userInput);
  JSON.parse(data);
  res.json({ accepted: true });
}
