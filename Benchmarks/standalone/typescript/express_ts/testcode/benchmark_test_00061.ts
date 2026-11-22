// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const BenchmarkTest00061 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  net.connect(80, new URL(String(data)).hostname);
  res.json({ accepted: true });
}
