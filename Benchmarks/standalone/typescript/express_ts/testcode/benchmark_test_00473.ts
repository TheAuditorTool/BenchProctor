// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const BenchmarkTest00473 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const data = nodeUtil.format("%s", userInput);
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
