// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { parseXmlString } from "libxmljs2";

export const BenchmarkTest00129 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body?.payload as string) || "";
  const data = String(userInput).slice(0, 200);
  parseXmlString(String(data), { noent: false, dtdload: false, nonet: true });
  res.json({ accepted: true });
}
