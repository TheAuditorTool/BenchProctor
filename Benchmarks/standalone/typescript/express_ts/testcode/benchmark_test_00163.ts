// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { parseXmlString } from "libxmljs2";

export const BenchmarkTest00163 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body?.multipart_field as string) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  parseXmlString(String(data), { noent: false, dtdload: false, nonet: true });
  res.json({ accepted: true });
}
