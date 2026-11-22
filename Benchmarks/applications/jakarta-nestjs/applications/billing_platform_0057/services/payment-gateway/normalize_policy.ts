// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("payment-gateway")
export class NormalizePolicy {
  @Post("normalizePolicy")
  async normalizePolicy(@Req() req: Request): Promise<unknown> {
    const caption = (req.body.field as string) || "";
    const remittance = decodeURIComponent(caption);
    const _clean = isoDompurify.sanitize(remittance);
    const dunning = _clean;
    return "<div>" + dunning + "</div>";
  }
}
