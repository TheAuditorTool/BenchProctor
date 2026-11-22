// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00095 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ accepted: true });
}
