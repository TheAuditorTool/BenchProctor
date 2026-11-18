// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";

export const BenchmarkTest00334 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true } as libxmljs.XMLParseOptions);
  res.json({ accepted: true });
}
