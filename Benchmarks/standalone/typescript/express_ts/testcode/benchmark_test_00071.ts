// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { parseXmlString } from "libxmljs2";

export const BenchmarkTest00071 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  parseXmlString(String(data), { noent: false, dtdload: false, nonet: true });
  res.json({ accepted: true });
}
