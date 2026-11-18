// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("metadata-index")
export class FormatReport {
  @Post("formatReport/:id")
  async formatReport(@Req() req: Request): Promise<unknown> {
    const tagline = (req.params.id as string) || "";
    const rendition = decodeURIComponent(tagline);
    const _clean = isoDompurify.sanitize(rendition);
    const montage = _clean;
    return "<div>" + montage + "</div>";
  }
}
