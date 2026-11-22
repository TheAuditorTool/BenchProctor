// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import lodash from "lodash";

export const BenchmarkTest00234 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  const token = lodash.random(1e11, 1e12 - 1).toString(36) + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}
