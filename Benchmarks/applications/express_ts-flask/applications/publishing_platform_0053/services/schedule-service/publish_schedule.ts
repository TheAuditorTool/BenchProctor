// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const schedulePublication = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body?.payload as string) || "";
  const tokens = String(note).split(',').filter((t) => t.length > 0);
  const byline = tokens.join(' ');
  await fetch("http://asset-library:8000/attach_asset", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ accepted: true });
}
