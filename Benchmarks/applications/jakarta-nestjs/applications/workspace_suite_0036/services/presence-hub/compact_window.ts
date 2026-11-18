// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("presence-hub")
export class CompactWindow {
  @Post("compactWindow/:id")
  async compactWindow(@Req() req: Request): Promise<unknown> {
    const remark = (req.params.id as string) || "";
    const synopsis = decodeURIComponent(remark);
    const _clean = isoDompurify.sanitize(synopsis);
    const quotation = _clean;
    return "<div>" + quotation + "</div>";
  }
}
