// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as vm from "node:vm";

export const BenchmarkTest00056 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  vm.runInNewContext(String(parsedNum), { Math });
  res.json({ accepted: true });
}
