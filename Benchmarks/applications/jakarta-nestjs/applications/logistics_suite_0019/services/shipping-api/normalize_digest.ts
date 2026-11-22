// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("shipping-api")
export class NormalizeDigest {
  @Post("normalizeDigest")
  async normalizeDigest(@Req() req: Request): Promise<unknown> {
    const citation = (req.body?.field as string) || "";
    const parcel = decodeURIComponent(citation);
    const _clean = isoDompurify.sanitize(parcel);
    const consignment = _clean;
    return "<div>" + consignment + "</div>";
  }
}
