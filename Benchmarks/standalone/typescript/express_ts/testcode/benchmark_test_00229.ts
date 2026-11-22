// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const BenchmarkTest00229 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const outbound = { method: "get", url: String(userInput), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
