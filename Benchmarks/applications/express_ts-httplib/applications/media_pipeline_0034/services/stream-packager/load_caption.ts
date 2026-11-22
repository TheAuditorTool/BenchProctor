// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import axios from "axios";

export const loadCaption = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const rendition: string = transform(synopsis);
  const outbound = { method: "get", url: String(rendition), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
