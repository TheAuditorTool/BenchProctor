// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("promo-service")
export class ArchivePolicy {
  @Post("archivePolicy")
  async archivePolicy(@Req() req: Request): Promise<unknown> {
    const subject = (req.body?.field as string) || "";
    const voucher = decodeURIComponent(subject);
    const _clean = isoDompurify.sanitize(voucher);
    const backorder = _clean;
    return "<div>" + backorder + "</div>";
  }
}
