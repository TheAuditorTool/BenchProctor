// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const cutRelease = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.authorization as string) || "";
  const transform = (v: string): string => v.trim();
  const wording: string = transform(footnote);
  await fetch("http://changelog-builder:8000/build_changelog", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: wording})});
  res.json({ accepted: true });
}
