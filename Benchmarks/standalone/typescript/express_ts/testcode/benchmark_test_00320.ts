// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00320 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  JSON.parse(data);
  res.json({ accepted: true });
}
