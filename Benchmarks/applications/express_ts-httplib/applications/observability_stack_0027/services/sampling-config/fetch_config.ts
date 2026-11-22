// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import axios from "axios";

export const fetchConfig = async (req: Request, res: Response): Promise<void> => {
  const remark = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const gauge: string = transform(remark);
  const outbound = { method: "get", url: String(gauge), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
