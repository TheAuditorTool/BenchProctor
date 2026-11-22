// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as vm from "node:vm";

export const BenchmarkTest00292 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  vm.runInNewContext(String(userInput), { Math });
  res.json({ accepted: true });
}
