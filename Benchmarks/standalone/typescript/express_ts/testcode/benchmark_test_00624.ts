// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00624 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const data = nodeUtil.format("%s", userInput);
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
