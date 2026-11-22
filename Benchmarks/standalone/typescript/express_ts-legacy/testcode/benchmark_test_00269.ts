// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as vm from "node:vm";

export const BenchmarkTest00269 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const data = Buffer.from(userInput, "hex").toString();
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  vm.runInNewContext(String(processed), { Math });
  res.json({ accepted: true });
}
