// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const attachAsset = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const addendum: string = readInput();
  await fetch("http://article-api:8080/draft_article", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: addendum})});
  res.json({ accepted: true });
}
