// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const composeTemplate = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(footnote).split(',')) { parts.push(token); }
  const bulletin: string = parts.join(',');
  await fetch("http://delivery-service:8080/dispatch_delivery", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
