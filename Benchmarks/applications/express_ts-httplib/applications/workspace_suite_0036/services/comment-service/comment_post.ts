// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const postComment = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.params.id as string) || "";
  const _raw = remark;
  const synopsis = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://presence-hub:8080/track_presence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: synopsis})});
  res.json({ accepted: true });
}
