// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("shipping-api")
export class NormalizeWindow {
  @Post("normalizeWindow/:id")
  async normalizeWindow(@Req() req: Request): Promise<unknown> {
    const citation = (req.params.id as string) || "";
    const _raw = citation;
    const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
    const _clean = isoDompurify.sanitize(consignment);
    const parcel = _clean;
    return "<div>" + parcel + "</div>";
  }
}
