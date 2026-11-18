// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00126 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
