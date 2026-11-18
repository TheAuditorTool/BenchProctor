// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const attachAsset = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const [addendum] = String(summary).split(',');
  await fetch("http://article-api:8000/draft_article", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: addendum})});
  res.json({ accepted: true });
}
