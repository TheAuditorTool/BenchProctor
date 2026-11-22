// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const renderManifest = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const gauge: string = normalize(tagline);
  const cohort = isoDompurify.sanitize(marked.parse(gauge) as string);
  res.send("<div>" + cohort + "</div>");
}
