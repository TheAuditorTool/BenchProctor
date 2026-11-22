// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as vm from "node:vm";

export const BenchmarkTest00301 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const [data] = String(userInput).split(',');
  vm.runInNewContext(String(data), { Math });
  res.json({ accepted: true });
}
