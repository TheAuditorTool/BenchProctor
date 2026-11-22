// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { parseXmlString } from "libxmljs2";

export const BenchmarkTest00342 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = `${userInput}`;
  parseXmlString(String(data), { noent: true, dtdload: true, nonet: false });
  res.json({ accepted: true });
}
