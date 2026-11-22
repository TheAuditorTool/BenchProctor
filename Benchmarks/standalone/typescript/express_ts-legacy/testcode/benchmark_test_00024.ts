// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";

export const BenchmarkTest00024 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const [data] = String(userInput).split(',');
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true } as libxmljs.XMLParseOptions);
  res.json({ accepted: true });
}
