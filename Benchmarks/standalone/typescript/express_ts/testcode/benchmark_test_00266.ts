// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";

export const BenchmarkTest00266 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body?.field as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  res.json({ accepted: true });
}
