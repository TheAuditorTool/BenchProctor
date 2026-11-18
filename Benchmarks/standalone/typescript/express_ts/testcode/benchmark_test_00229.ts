// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00229 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-forwarded-for"] as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
