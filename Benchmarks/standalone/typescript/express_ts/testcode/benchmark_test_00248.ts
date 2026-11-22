// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as vm from "node:vm";

export const BenchmarkTest00248 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.origin as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  vm.runInNewContext(String(data), { Math });
  res.json({ accepted: true });
}
