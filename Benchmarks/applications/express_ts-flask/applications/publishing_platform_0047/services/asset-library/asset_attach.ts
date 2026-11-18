// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const attachAsset = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.referer as string) || "";
  const payload = { get value() { return synopsis; } };
  const byline = payload.value;
  await fetch("http://syndication-feed:8000/push_syndication", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ accepted: true });
}
