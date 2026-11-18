// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const trackPresence = async (req: Request, res: Response): Promise<void> => {
  const preface = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const remark: string = normalize(preface);
  await fetch("http://share-service:8080/grant_share", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: remark})});
  res.json({ accepted: true });
}
