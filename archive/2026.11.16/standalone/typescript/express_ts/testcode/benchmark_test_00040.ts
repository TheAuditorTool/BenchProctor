// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const BenchmarkTest00040 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const data = nodeUtil.format("%s", userInput);
  const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + processed + "</div>");
}
