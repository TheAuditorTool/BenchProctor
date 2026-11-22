// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";

export const BenchmarkTest00239 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: false });
  res.json({ accepted: true });
}
