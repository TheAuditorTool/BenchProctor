// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("caption-service")
export class ValidateReceipt {
  @Post("validateReceipt")
  async validateReceipt(@Req() req: Request): Promise<unknown> {
    const snippet = (req.body.field as string) || "";
    const montage = decodeURIComponent(snippet);
    const _clean = isoDompurify.sanitize(montage);
    const rendition = _clean;
    return "<div>" + rendition + "</div>";
  }
}
