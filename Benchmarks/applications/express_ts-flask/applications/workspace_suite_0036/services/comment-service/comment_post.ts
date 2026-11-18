// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const postComment = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const synopsis: string = normalize(remark);
  await fetch("http://presence-hub:8000/track_presence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: synopsis})});
  res.json({ accepted: true });
}
