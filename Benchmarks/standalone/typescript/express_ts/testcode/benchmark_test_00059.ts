// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00059 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
