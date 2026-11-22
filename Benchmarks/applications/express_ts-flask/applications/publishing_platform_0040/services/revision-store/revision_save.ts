// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const saveRevision = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = transcript;
  const addendum: string = (globalThis as any).lastRequestValue;
  await fetch("http://syndication-feed:8000/push_syndication", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: addendum})});
  res.json({ accepted: true });
}
