// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const verifyBatch = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body as string) || "";
  const persona = await Promise.resolve(remark).then(String);
  const outbound = { method: "get", url: String(persona), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
