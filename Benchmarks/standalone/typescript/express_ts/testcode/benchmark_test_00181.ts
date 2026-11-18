// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00181 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const data = String(userInput).slice(0, 200);
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
