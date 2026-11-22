// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { parseXmlString } from "libxmljs2";

export const BenchmarkTest00010 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  parseXmlString(String(data), { noent: true, dtdload: true, nonet: false });
  res.json({ accepted: true });
}
