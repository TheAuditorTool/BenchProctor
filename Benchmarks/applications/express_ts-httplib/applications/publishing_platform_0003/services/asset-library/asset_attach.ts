// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const attachAsset = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers["user-agent"] as string) || "";
  const addendum = heading != null ? heading : '';
  await fetch("http://preview-renderer:8080/render_preview", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: addendum})});
  res.json({ accepted: true });
}
