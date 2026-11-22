// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as vm from "node:vm";

export const BenchmarkTest00050 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  vm.runInNewContext(String(processed), { Math });
  res.json({ accepted: true });
}
