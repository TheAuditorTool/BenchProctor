// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const BenchmarkTest00157 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const data = userInput != null ? userInput : '';
  const outbound = { method: "get", url: String(data), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
