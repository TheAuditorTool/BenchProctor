// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import lodash from "lodash";

export const BenchmarkTest00258 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = String(userInput).slice(0, 200);
  const token = lodash.random(1e11, 1e12 - 1).toString(36) + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}
