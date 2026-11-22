// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const loadBundle = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.authorization as string) || "";
  const inquiry = String(remark).slice(0, 200);
  const outbound = { method: "get", url: String(inquiry), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
