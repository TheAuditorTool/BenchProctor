// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const reconcileWindow = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body as string) || "";
  const remittance = await Promise.resolve(headline).then(String);
  const outbound = { method: "get", url: String(remittance), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
